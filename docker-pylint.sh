#!/bin/bash
# this file is used to run pylint from within emacs pylint command, see .dir-locals.el file for config details
# slashes in project_directory path should be escaped with backslash /home/projects/name -> \/home\/projects\/name
cd /home/user/app
pylint $1 $2 ${3/{{project_directory}}/\/home\/user\/app}
