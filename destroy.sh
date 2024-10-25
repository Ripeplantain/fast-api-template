#!/bin/bash
docker-compose down
docker image rm $(docker images) -f