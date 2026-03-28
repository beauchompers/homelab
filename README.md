# homelab

Collection of Ansible roles for my Homelab infrastructure.

## Requirements

- Ansible core 2.20+
- Collections:
  - `ansible.posix`
  - `community.docker`

Install collections with:

```bash
ansible-galaxy collection install ansible.posix community.docker
```

## Quick Start

1. Create an inventory file with your hosts
2. Set required variables (see each role's README for details)
3. Run a playbook:

```bash
ansible-playbook -i inventory.ini homelab-setup-common.yml
```

## Ansible Roles

| Role | Description |
| --- | --- |
| [homelab-common](homelab-common/) | Base configuration for VMs (SSH keys, sudo, packages, hostname) |
| [homelab-containers](homelab-containers/) | Install Docker or Podman depending on the server OS |
| [homelab-k3s](homelab-k3s/) | Install and configure a K3s Kubernetes cluster |
| [homelab-container-registry](homelab-container-registry/) | Deploy a private Docker registry with TLS |
| [homelab-nginx](homelab-nginx/) | Install and configure an NGINX load balancer |
| [homelab-elasticsearch-docker](homelab-elasticsearch-docker/) | Deploy an Elasticsearch cluster using Docker Compose (single or 3-node) |
| [homelab-splunk](homelab-splunk/) | Deploy a Splunk container with SSL/TLS support |

See each role's README for variables, requirements, and example playbooks.

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

## Kubernetes Deployments

The `kubernetes-deployments/` directory contains K8s manifests for:
- Elasticsearch cluster
- AWX (Ansible Tower)
- OWASP Juice Shop

## Archived

Retired roles and scripts are in the `archive/` directory for reference:
- homelab-microk8s, homelab-berries, homelab-nfs-server, homelab-nfs-client
- proxmox-helper.py, Dockerfiles

## Author

Mike Beauchamp (beauchompers)
