# homelab-common

Base configuration role for homelab VMs. Installs OS packages, configures SSH key access, passwordless sudo, and sets the hostname.

## Supported Platforms

- Ubuntu
- Debian / Kali
- CentOS / Rocky / AlmaLinux / RHEL

## Role Variables

| Variable | Default | Description |
| --- | --- | --- |
| `login_user` | `""` | User account to configure on the target VM |
| `local_user` | `""` | Local user whose SSH public key will be deployed |
| `home_dir_path` | `""` | Home directory path prefix (e.g., `home` for `/home/`) |

## What It Does

1. Installs base packages per OS (sudo, python3, qemu-guest-agent)
2. Upgrades all packages to latest
3. Deploys your SSH public key for `login_user`
4. Adds `login_user` to sudoers (passwordless)
5. Sets hostname to match inventory hostname
6. (CentOS/Rocky) Disables firewalld, adds systemd service files for RHEL

## Example Playbook

```yaml
---
- name: Apply common configuration
  hosts: common
  serial: 4
  become: true
  tasks:
    - name: Add Common Configuration
      ansible.builtin.import_role:
        name: homelab-common
```

## Author

Mike Beauchamp (beauchompers)
