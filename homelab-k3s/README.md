# homelab-k3s

Installs a K3s Kubernetes cluster with a server (control plane) node and worker nodes.

## Supported Platforms

- Ubuntu
- Debian

## Requirements

- The `homelab-containers` role should be applied first (for Docker)
- Nodes must be able to reach each other on port 6443

## What It Does

1. Installs `iptables-persistent` and `nfs-common`
2. Sets iptables FORWARD policy to ACCEPT
3. Installs K3s on the first host in the play (server node) using containerd
4. Retrieves the cluster join token from the server node
5. Joins remaining hosts as worker nodes
6. Uses `creates: /usr/local/bin/k3s` for idempotency

The first host in your `k3s_cluster` inventory group becomes the server node. All others join as workers.

## Example Playbook

```yaml
---
- name: Configure /etc/hosts for K3s cluster
  hosts: k3s_cluster
  become: true
  tasks:
    - name: Update the /etc/hosts file with node name
      ansible.builtin.lineinfile:
        path: /etc/hosts
        regexp: ".*\t{{ hostvars[item]['ansible_hostname'] }}\t{{ hostvars[item]['ansible_hostname'] }}"
        line: "{{ hostvars[item]['ansible_default_ipv4']['address'] }}\t{{ hostvars[item]['ansible_hostname'] }}"
        state: present
      with_items: "{{ groups['k3s_cluster'] }}"

- name: Install Docker and K3s on cluster nodes
  hosts: k3s_cluster
  serial: 1
  become: true
  tasks:
    - name: Install Docker
      ansible.builtin.import_role:
        name: homelab-containers

    - name: Install K3s
      ansible.builtin.import_role:
        name: homelab-k3s
```

## Author

Mike Beauchamp (beauchompers)
