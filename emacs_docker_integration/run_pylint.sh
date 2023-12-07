#!/bin/bash
output=$(docker exec -i $CONTAINER_NAME python3 $1 "$2" $3 $4 ${5/$PROJECT_ROOT/$CONTAINER_ROOT} ${6/$PROJECT_ROOT/$CONTAINER_ROOT})
echo $output
exit 0
