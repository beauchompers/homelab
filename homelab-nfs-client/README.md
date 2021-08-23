Homelab NFS Client
=========

This role installs the NFS client tools, and mounts the share from the NFS server. 

Requirements
------------

None, although you can use this with my homelab-nfs-server role.

Role Variables
--------------

nfs_share: ""
- The share to mount on, example /data

nfs_server_share: ""
- The share on the nfs server, example /nfsshare

nfs_server: ""
- The hostname or IP of the nfs server.

Dependencies
------------

None.

Example Playbook
----------------

```
---
- hosts: nfs_client
  become: yes
  vars:
    nfs_share: "/data/"
    nfs_server_share: "/nfsshare"
    nfs_server: "nfsserver01"
  tasks:
    - name: Setup NFS Clients
      import_role:
        name: homelab-nfs-client


License
-------

BSD

Author Information
------------------

Mike Beauchamp (beauchompers)
