Homelab - NGINX
=========

This role installs NGINX as a Load Balancer with the backends being a group in inventory.

Requirements
------------

None

Role Variables
--------------

conf_name: name of the nginx configuration template to deploy from the templates dir.
server_group_name: backend server group in the above conf file
server_group: ansible inventory group for the backend servers in the conf file. 
cert_file: certificate file for nginx.
key_file: private key for the above certificate.

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: load_balancer
  become: yes
  vars:
    conf_name: "demisto.conf"
    server_group_name: "demisto"
    server_group: "demisto_app_servers"
    cert_file: "cert.crt"
    key_file: "cert.key"
  tasks:
    - name: Setup NGINX Load Balancer
      import_role:
        name: homelab-nginx
```

License
-------

BSD

Author Information
------------------

Mike Beauchamp (beauchompers)

