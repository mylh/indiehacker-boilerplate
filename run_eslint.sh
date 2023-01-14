#!/bin/bash
docker exec -it {{project_name}}_web npx eslint $@
