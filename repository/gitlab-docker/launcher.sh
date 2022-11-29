#!/bin/bash

sudo docker run --detach \
    --hostname 0.0.0.0 \
    --publish 443:443 --publish 80:80 --publish 22:22 \
    --name gitlab \
    --restart always \
    --v gitlab_config:/etc/gitlab \
    --v gitlab_logs:/var/log/gitlab \
    --v gitlab_data:/var/opt/gitlab \
    --shm-size 256m \
    gitlab/gitlab-ce:latest
