# homelab-containers

Installs and configures Docker or Podman depending on the target OS.

## Supported Platforms

**Docker:**
- Ubuntu
- Debian
- CentOS 7
- Amazon Linux 2

**Podman:**
- CentOS 8+
- Rocky Linux
- AlmaLinux
- RHEL 8+

## Role Variables

| Variable | Default | Description |
| --- | --- | --- |
| `docker_compose_install` | `false` | Install the Docker Compose v2 plugin |
| `insecure_registry` | `false` | Configure an insecure Docker registry |
| `insecure_registry_name` | `""` | Hostname of the insecure registry |

## What It Does

1. Detects system architecture (amd64/arm64)
2. Installs Docker CE from official Docker repos (Debian-family, CentOS 7, Amazon Linux) or Podman (RHEL 8+ family)
3. Starts and enables the container engine service
4. Optionally installs Docker Compose as a CLI plugin (`docker compose`)
5. Optionally configures an insecure registry in Docker daemon config

## Example Playbook

```yaml
---
- name: Install container engine
  hosts: containers
  become: true
  tasks:
    - name: Setup Container Engine
      ansible.builtin.import_role:
        name: homelab-containers
      vars:
        docker_compose_install: true
```

## Author

Mike Beauchamp (beauchompers)
