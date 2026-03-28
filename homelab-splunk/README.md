# homelab-splunk

Deploys a Splunk Enterprise container with SSL/TLS support.

## Supported Platforms

- Ubuntu
- Debian

## Requirements

- The `homelab-containers` role should be applied first (for Docker)
- TLS certificate and key files placed in the role's `files/` directory

## Role Variables

| Variable | Default | Description |
| --- | --- | --- |
| `splunk_password` | `"changeme"` | Splunk admin password |
| `splunk_port` | `"8000"` | Splunk web UI port |
| `splunk_dir` | `""` | Directory on the target for Splunk data and certs |
| `splunk_cert` | `""` | Certificate filename for SSL |
| `splunk_key` | `""` | Private key filename for SSL |

## What It Does

1. Creates the Splunk directory on the target
2. Copies TLS certificate and key
3. Starts the `splunk/splunk:latest` container with SSL enabled

### Exposed Ports

| Port | Service |
| --- | --- |
| 8000 | Splunk Web UI |
| 8065 | Splunk App Server |
| 8088 | HTTP Event Collector (HEC) |
| 8089 | Splunk Management |
| 8191 | KV Store |
| 9887 | Splunk-to-Splunk |
| 9997 | Splunk Forwarder Receiving |

## Example Playbook

```yaml
---
- name: Setup Splunk with Docker
  hosts: splunk
  become: true
  vars_files:
    - extra-vars-splunk.yml
  tasks:
    - name: Setup Container Engine
      ansible.builtin.import_role:
        name: homelab-containers

    - name: Setup Splunk
      ansible.builtin.import_role:
        name: homelab-splunk
```

## Author

Mike Beauchamp (beauchompers)
