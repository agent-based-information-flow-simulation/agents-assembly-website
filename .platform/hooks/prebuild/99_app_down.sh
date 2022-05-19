#!/bin/bash

# t2.micro instances are not powerful enough to handle
# the application and the build process running simultaneously
# they simply turn off (thus increasing timeout limit to maximum didn't help)
# more elegant solutions would require using a more expensive instance type
# i.e. t2.small or AWS CodePipeline (additional costs)
# this solution introduces a tiny downtime during the build process

#DOCKER_PROCESS_COUNT=`docker ps -q | wc -l`
#if [ "$DOCKER_PROCESS_COUNT" -gt 0 ]; then docker stop --time 30 $(docker ps -q); fi

# if this script returns a non-zero value then the instance loops itself
# trying to run the prebuild scripts indefinitely
# so if 'docker stop' fails then the build process should continue and
# potentially fail later due to having not enough memory
#exit 0
