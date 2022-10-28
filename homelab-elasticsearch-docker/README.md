Homelab Elasticsearch 
=========

Installs an Elasticsearch Cluster or Single Node using Docker on the target server. From: [Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html).

Requirements
------------

Tested on Ubuntu 20.04.02 LTS

Role Variables
--------------

elastic_username: "elastic"
- Username for the elastic cluster

elastic_password: "changeme"
- Password for the elastic user

cluster_type: "single | cluster"
- Whether to create a single node cluster, or a 4 node cluster using Docker
- Cluster is 3 nodes with all roles and one coordinating node, and kibana.

elastic_memory: "512"
- The Xms/Xmx memory for each container, increase based on your server specs

elastic_version: "7.17.1"
- The version of elastic to run for each container.

elastic_api_key: true | false (default is false)
- Used when you want to create an API Key when starting the cluster

elastic_url: "https://es01:9200"
- The URL for an elastic node, used to create the key

elastic_api_key_file_name: ""
- The JSON file for the privleges to create the key with
- See the elastic-api-key-example.json file for reference.

Dependencies
------------

Include the homelab-container role as a prereq for Docker.

Example Playbook
----------------

```
---
- hosts: elastic
  become: yes
  vars: 
    elastic_password: "Password1"
    cluster_type: "cluster"
    elastic_memory: "2048"
  tasks:
    - name: Install Docker
      import_role:
        name: homelab-containers

    - name: Setup Elasticsearch Node with Docker Compose
      import_role:
        name: homelab-elasticsearch-docker
```

License
-------

BSD

Author Information
------------------

Mike Beauchamp (beauchompers)
