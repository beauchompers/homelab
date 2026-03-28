# homelab-nginx

Installs NGINX and configures it as a TLS-enabled load balancer using a Jinja2 template.

## Supported Platforms

- Ubuntu
- Debian

## Role Variables

| Variable | Default | Description |
| --- | --- | --- |
| `conf_name` | `""` | Name of the NGINX config template (without `.j2`) to deploy |
| `server_group_name` | `""` | Backend server group name used in the config template |
| `server_group` | `""` | Ansible inventory group for backend servers |
| `cert_file` | `""` | Certificate filename (placed in role's `files/` directory) |
| `key_file` | `""` | Private key filename (placed in role's `files/` directory) |

## What It Does

1. Installs NGINX via apt
2. Copies TLS certificate and key to `/etc/nginx/`
3. Deploys the NGINX config from `templates/{{ conf_name }}.j2` to `/etc/nginx/conf.d/`
4. Restarts NGINX on config or cert changes

## Example Playbook

```yaml
---
- name: Setup load balancer
  hosts: load_balancer
  become: true
  tasks:
    - name: Setup NGINX Load Balancer
      ansible.builtin.import_role:
        name: homelab-nginx
      vars:
        conf_name: "myapp.conf"
        server_group_name: "myapp"
        server_group: "app_servers"
        cert_file: "cert.crt"
        key_file: "cert.key"
```

## Author

Mike Beauchamp (beauchompers)
