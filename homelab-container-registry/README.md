# homelab-container-registry

Deploys a private Docker registry (registry:2) with TLS using self-signed certificates.

## Supported Platforms

- Ubuntu
- Debian

## Requirements

- The `homelab-containers` role should be applied first (for Docker)
- A self-signed certificate and key matching the target hostname, placed in the role's `files/` directory as `<hostname>.cer` and `<hostname>.key`

## What It Does

1. Creates `/certs` directory on the target
2. Copies the TLS certificate and key
3. Starts a `registry:2` container with HTTPS on port 443

## Example Playbook

```yaml
---
- name: Setup container registry
  hosts: container_registry
  become: true
  tasks:
    - name: Install Docker
      ansible.builtin.import_role:
        name: homelab-containers

    - name: Create Container Registry
      ansible.builtin.import_role:
        name: homelab-container-registry
```

## Author

Mike Beauchamp (beauchompers)
