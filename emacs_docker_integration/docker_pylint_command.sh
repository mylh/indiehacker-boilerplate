#!/bin/bash

# Ensure CONTAINER_NAME is set
if [ -z "$CONTAINER_NAME" ]; then
    echo "Error: CONTAINER_NAME is not set"
    exit 1
fi

# Prepare the arguments for pylint
args=()
for arg in "$@"; do
    if [[ $arg == $PROJECT_ROOT* ]]; then
        args+=("${arg/$PROJECT_ROOT/$CONTAINER_ROOT}")
    else
        args+=("$arg")
    fi
done

# Run pylint in the Docker container
output=$(docker exec -i "$CONTAINER_NAME" pylint "${args[@]}")

# Output the result
echo "$output"

# Exit with the same status code as pylint
exit $?
