from time import sleep
import requests
import argparse
import configparser

urllib3 = requests.packages.urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# utility functions
def get_ticket(username, password):
    """
    Gets the authentication cookie and csrf token from the proxmox API
    """
    data = {
        "username":username,
        "password":password
    }

    res = requests.post(f"{base_url}/access/ticket", json=data, verify=False)

    csrf_token = res.json().get("data").get("CSRFPreventionToken")
    ticket = res.json().get("data").get("ticket")
    
    return csrf_token, ticket


def proxmox_request(method, csrf_token, ticket, uri):
    """
    Requests handler for the API
    """
    headers = {
        "CSRFPreventionToken": csrf_token
    }

    cookies = {
        "PVEAuthCookie": ticket
    }
        
    if method == "GET":
        res = requests.get(f"{base_url}/{uri}", headers=headers, cookies=cookies, verify=False)
    if method == "POST":
        res = requests.post(f"{base_url}/{uri}", headers=headers, cookies=cookies, verify=False)
    return res.json()


def get_running(all_nodes):
    """
    Gets the list of currently running nodes, and returns the name and ID
    """
    running = []
    for node in all_nodes:
        if node.get("status") == "running":
            running.append({ "node":node.get("name"),"id":node.get("vmid")})
        
    return running
 

def get_node_ids(all_nodes, nodes):
    """
    Gets the vm id of the provided nodes, and returns the list of ids
    """
    node_ids = []
    for node in all_nodes:
        if node.get("name") in nodes:
            node_ids.append({"node":node.get("name"),"id":node.get("vmid")})
        
    return node_ids

 
def rollback_snapshot(nodes, snapshot, csrf, ticket):
    """
    Rolls back the provided node ids to the provided snapshot
    # POST /api2/json/nodes/{nodename}/qemu/{vmid}/snapshot/{snapname}/rollback
    """

    results = []
    for node in nodes:
        res = proxmox_request("POST", csrf, ticket, f"/nodes/{nodename}/qemu/{node}/snapshot/{snapshot}/rollback")
        results.append(node)
    return results

def start_vm(nodes, csrf, ticket):
    """
    Starts the provided node ids
    # POST /api2/json/nodes/{nodename}/qemu/{vmid}/status/start
    """

    results = []
    for node in nodes:
        res = proxmox_request("POST", csrf, ticket, f"/nodes/{nodename}/qemu/{node}/status/start")
        results.append(node)
    return results

def stop_vm(nodes, csrf, ticket):
    """
    Stops the provided node ids
    # POST /api2/json/nodes/{nodename}/qemu/{vmid}/status/stop
    """
 
    results = []
    for node in nodes:
        res = proxmox_request("POST", csrf, ticket, f"/nodes/{nodename}/qemu/{node}/status/stop")
        results.append(node)
    return results

# MAIN

# Read config file
config = configparser.ConfigParser()
config.read('proxmox-config.ini')

username = config["DEFAULT"]["username"]
password = config["DEFAULT"]["password"]
base_url = config["DEFAULT"]["base_url"]
nodename = config["DEFAULT"]["nodename"]
snapshot = config["DEFAULT"]["snapshot"]
quick_configs = config["QUICK_SETUPS"]["quick_configs"].split(",")

# proxmox-helper args
arg_parser = argparse.ArgumentParser(description='Homelab Proxmox Helper, because clicking is not efficient')
arg_parser.add_argument('--nodes', dest='nodes', help='List of Node names, example --nodes=node1,node2,node3')
arg_parser.add_argument('--action', dest='action', choices=['start','stop','rollback','rollbackall','stopall'], default='rollback', help='Actions to take on the nodes, if rollback it will rollback the started vms to the provided snapshot.')
arg_parser.add_argument('--snapshot', dest='snapshot', default=snapshot, help='Which snapshot to rollback the nodes to.')
arg_parser.add_argument('--quick', dest='quick', choices=quick_configs, default=None, help='list of quick setups from the config file')
args = arg_parser.parse_args()

# authenticate to api
csrf, ticket = get_ticket(username,password)

#get all nodes
all_nodes = proxmox_request("GET",csrf, ticket, f"/nodes/{nodename}/qemu")["data"]

# check we got some nodes
if args.nodes:
    nodes = args.nodes.split(",")
    node_ids = [x.get("id") for x in get_node_ids(all_nodes,nodes)]
else:
    nodes = None

# quick config, rollback and start the selected nodes 
if args.quick:
    # get running nodes
    node_ids = [ x.get("id") for x in get_running(all_nodes)]
    
    # stop vms
    stopped_vms = stop_vm(node_ids, csrf, ticket)
    print(f"Stopped: {stopped_vms}")
    sleep(10)
    
    nodes = config["QUICK_SETUPS"][args.quick].split(",")
    node_ids = [x.get("id") for x in get_node_ids(all_nodes,nodes)]
    
    # rollback
    snapshots = rollback_snapshot(node_ids, args.snapshot, csrf, ticket)
    print(f"Rolled back: {snapshots}")
    sleep(10)

    # start vms after rollback
    started_vms = start_vm(node_ids, csrf, ticket)
    sleep(10)
    print(f"Started: {started_vms}")

if args.action == "rollback" and not args.quick:
    # get running nodes
    node_ids = [ x.get("id") for x in get_running(all_nodes)]
    
    # rollback
    snapshots = rollback_snapshot(node_ids, args.snapshot, csrf, ticket)
    print(f"Rolled back: {snapshots}")
    sleep(10)

    # start vms after rollback
    started_vms = start_vm(node_ids, csrf, ticket)
    sleep(10)
    print(f"Started: {started_vms}")

if args.action == "rollbackall" and not args.quick:
    # get running nodes
    node_ids = [ x.get("vmid") for x in all_nodes ]
    
    # rollback
    snapshots = rollback_snapshot(node_ids, args.snapshot, csrf, ticket)
    print(f"Rolled back: {snapshots}")
    
if args.action == "start" or args.action == "stop":
    if not node_ids:
        # handle no nodes
        print("Must provide --nodes argument")
    
    if args.action == "start":
        # start vms
        started_vms = start_vm(node_ids, csrf, ticket)
        print(f"Started: {started_vms}") 
    
    if args.action == "stop":
        # stop vms
        stopped_vms = stop_vm(node_ids, csrf, ticket)
        print(f"Stopped: {stopped_vms}") 
    
if args.action == "stopall":
    # get running nodes
    node_ids = [ x.get("id") for x in get_running(all_nodes)]
    
    # stop vms
    stopped_vms = stop_vm(node_ids, csrf, ticket)
    print(f"Stopped: {stopped_vms}") 
    