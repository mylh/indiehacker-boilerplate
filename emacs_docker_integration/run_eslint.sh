#!/bin/bash
output=$(docker exec -i $CONTAINER_NAME npx eslint ${1/$PROJECT_ROOT/$CONTAINER_ROOT} ${2/$PROJECT_ROOT/$CONTAINER_ROOT} ${3/$PROJECT_ROOT/$CONTAINER_ROOT} $4 $5 $6 $7 $8 $9)
echo -e "$output"
exit 0
