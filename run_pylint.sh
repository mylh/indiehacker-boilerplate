#!/bin/bash
# this file is used to run pylint from within emacs pylint command, see .dir-locals.el file for config details
# slashes in project_directory path should be escaped with backslash /home/projects/name -> \/home\/projects\/name
output=$(docker exec -i {{ project_name }}_web python3 $1 "$2" $3 $4 ${5/{{project_directory}}/\/app} ${6/\{{project_directory}}/\/app})
echo $output
exit 0
