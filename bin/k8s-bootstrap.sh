#!/usr/bin/env bash

name=tutorial
cluster=europe-west2-a
node_number=1
machine_type=n1-standard-1

# 1. Create cluster
gcloud beta container clusters create ${name} \
    --zone ${cluster} \
    --num-nodes ${node_number} \
    --machine-type ${machine_type} \
    --scopes "cloud-platform,storage-ro,logging-write,monitoring-write,service-control,service-management,https://www.googleapis.com/auth/ndev.clouddns.readwrite"

# 2. Save cluster credentials
gcloud container clusters get-credentials ${name} --zone ${cluster}
