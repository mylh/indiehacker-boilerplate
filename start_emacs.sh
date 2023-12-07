export CONTAINER_NAME={{project_name}}_web
export PROJECT_ROOT=$(pwd)
export CONTAINER_ROOT=/home/user/app
DESKTOP_DIR=$(pwd)
emacs --eval="(desktop-change-dir \"$DESKTOP_DIR\")"

