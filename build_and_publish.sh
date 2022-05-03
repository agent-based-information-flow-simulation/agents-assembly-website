#!/bin/bash
docker-compose -f docker-compose.build.yml build --parallel
docker-compose -f docker-compose.build.yml push
