# homelab

Collection of Ansible Roles and helper scripts I use for my Homelab.  

## Ansible Roles

The following roles are in this repo. 

| Role | Description | 
| --- | --- |
| homelab-common | Role to apply a common config for my VMs |
| homelab-containers | Role to install Docker or Podman depending on the server OS |
| homelab-elasticsearch-docker | Role to install an Elasticsearch cluster using Docker, either cluster (3), or single node |
| homelab-nfs-client | Role to install NFS and mount a directory on the target servers | 
| homelab-nfs-server | Role to install an NFS server to serve the above ones! |

## Scripts

The following helper scripts are in here:

| Script | Description |
| --- | --- | 
| ```proxmox-helper.py``` | Starts, Stops, Rollback, or quickly setup the VMs I want to use with the roles etc! | 

