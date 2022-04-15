Homelab Containers
=========

This role installs and configures the required container engine, be it Docker or Podman depending on the OS.

Tested with the following Operating Systems.

Docker:
- Ubuntu 20.04.02 LTS
- Debian 10 (Buster)
- Centos 7
- Amazon Linux 2

Podman:
- RedHat 8
- Centos 8
- Rocky Linux
- AlmaLinux

Requirements
------------

Docker installation uses the Docker CE repos, while Podman is from the repos for the above operating systems. 

Role Variables
--------------

Following variables can be defined, which allows for the installation of docker compose as well:

docker_compose_install: false
docker_compose_version: "1.29.2"
docker_compose_url: https://github.com/docker/compose/releases/download/{{ docker_compose_version }}/docker-compose-Linux-x86_64
docker_compose_path: /usr/local/bin/docker-compose
insecure_registry: false
insecure_registry_name: myregistry

Dependencies
------------

None

Example Playbook
----------------

Usage as per below:

```
- hosts: all
  become: yes
  vars:
    docker_compose_install: true
    docker_compose_veresion: "1.29.2"
    docker_compose_url: https://github.com/docker/compose/releases/download/{{ docker_compose_version }}/docker-compose-Linux-x86_64
    docker_compose_path: /usr/local/bin/docker-compose
  tasks:
    - name: Setup Container Engine
      import_role:
        name: homelab-containers
```


License
-------

BSD

Author Information
------------------

Mike Beauchamp (beauchompers)

