# homelab-elasticsearch-docker

Deploys an Elasticsearch cluster (single node or 3-node) with Kibana using Docker Compose, including TLS encryption.

## Supported Platforms

- Ubuntu
- Debian

## Requirements

- The `homelab-containers` role should be applied first (for Docker)
- Docker Compose v2 plugin installed (`docker_compose_install: true` on the containers role)

## Role Variables

| Variable | Default | Description |
| --- | --- | --- |
| `elastic_username` | `"elastic"` | Elasticsearch admin username |
| `elastic_password` | `"changeme"` | Elasticsearch admin password |
| `cluster_type` | `"single"` | `"single"` for one node, anything else for 3-node cluster |
| `elastic_memory` | `"512"` | JVM heap size in MB per node (Xms/Xmx) |
| `elastic_version` | `"7.17.1"` | Elasticsearch/Kibana version |
| `elastic_url` | `""` | Elasticsearch URL (for API key creation) |
| `elastic_api_key` | `false` | Whether to create API keys on startup |
| `elastic_api_key_file_name` | `""` | JSON file defining API key privileges |

## What It Does

1. Sets `vm.max_map_count` sysctl for cluster mode
2. Copies Docker Compose project files to the target
3. Renders the appropriate Compose template (single or cluster)
4. Generates TLS certificates using Elasticsearch's built-in certutil
5. Brings up the Elasticsearch + Kibana stack
6. Optionally creates API keys via the Elasticsearch REST API

### Cluster Topology

- **Single mode:** 1 Elasticsearch node + Kibana
- **Cluster mode:** 3 Elasticsearch nodes (es01, es02, es03) + Kibana, with full TLS between nodes

## Example Playbook

```yaml
---
- name: Setup Elasticsearch with Docker
  hosts: elastic
  become: true
  tasks:
    - name: Install Docker
      ansible.builtin.import_role:
        name: homelab-containers
      vars:
        docker_compose_install: true

    - name: Setup Elasticsearch Node with Docker Compose
      ansible.builtin.import_role:
        name: homelab-elasticsearch-docker
      vars:
        elastic_password: "MySecurePassword"
        cluster_type: "cluster"
        elastic_memory: "2048"
```

## Author

Mike Beauchamp (beauchompers)
