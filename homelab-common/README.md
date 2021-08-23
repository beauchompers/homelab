Homelab Common
=========

Common configuration for homelab servers.  Installation of packages for OS and Proxmox, as well as setting up SSH and sudo access quickly. 

Requirements
------------
None


Role Variables
--------------

login_user: ""
- User to login as

local_user: ""
- Local user to create and add to sudoers.

Dependencies
------------

None.

Example Playbook
----------------

```
---
- hosts: common
  become: yes
  tasks:
    - name: Add Common Configuration
      import_role:
        name: homelab-common
    
    - name: Shutdown VM
      ansible.builtin.command:
        cmd: "shutdown -h +1"
      tags:
        - shutdown
```

License
-------

BSD

Author Information
------------------

Mike Beauchamp (beauchompers)