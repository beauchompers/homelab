Homelab NFS Server
=========

This role installs an NFS server, and a default share /nfsshare

Requirements
------------

None

Role Variables
--------------

nfs_exports: ["/nfsshare *(rw,sync,no_root_squash,no_all_squash)"]
- The share to export in /etc/exports

Dependencies
------------

None

Example Playbook
----------------

Example to setup the server:

```
---
- hosts: nfs
  become: yes
  tasks:
    - name: Setup NFS Server
      import_role:
        name: homelab-nfs-server
```


License
-------

BSD

Author Information
------------------

Mike Beauchamp (beauchompers)