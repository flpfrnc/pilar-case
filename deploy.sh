#!/usr/bin/bash

# stop any existing containers
docker-compose down

docker-compose pull

# recreate containers
docker-compose up -d
