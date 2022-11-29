#!/bin/bash

sudo docker run \
    -v sonarqube_data:/opt/sonarqube/data \
    -v sonarqube_extensions:/opt/sonarqube/extensions \
    -v sonarqube_logs:/opt/sonarqube/logs \
    --name="sonarqube" -p 9000:9000 sonarqube:community
