# homelab

Collection of Ansible roles for my Homelab infrastructure.

Requires Ansible core 2.20+ and the following collections:
- `ansible.posix`
- `community.docker`

## Ansible Roles

| Role | Description |
| --- | --- |
| homelab-common | Base configuration for VMs (SSH keys, sudo, packages, hostname) |
| homelab-containers | Install Docker or Podman depending on the server OS |
| homelab-k3s | Install and configure a K3s Kubernetes cluster |
| homelab-container-registry | Deploy a private Docker registry with TLS |
| homelab-nginx | Install and configure an NGINX load balancer |
| homelab-elasticsearch-docker | Deploy an Elasticsearch cluster using Docker Compose (single or 3-node) |
| homelab-splunk | Deploy a Splunk container with SSL/TLS support |

## Playbooks

| Playbook | Description |
| --- | --- |
| `homelab-setup-common.yml` | Apply common config and reboot |
| `homelab-containers.yml` | Install Docker on container and registry hosts |
| `homelab-container-engine.yml` | Install Docker on container hosts only |
| `homelab-container-registry.yml` | Setup a private Docker registry |
| `homelab-k3s-setup.yml` | Bootstrap a K3s cluster |
| `homelab-elastic-setup.yml` | Deploy Elasticsearch with Docker |
| `homelab-splunk.yml` | Deploy Splunk with Docker |
| `homelab-gather-facts.yml` | Gather and print facts from all hosts |

## Archived

Retired roles and scripts are in the `archive/` directory for reference:
- homelab-microk8s, homelab-berries, homelab-nfs-server, homelab-nfs-client
- proxmox-helper.py, Dockerfiles
