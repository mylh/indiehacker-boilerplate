# Indiehacker Boilerplate

## About

Django project template with many useful libraries and integrations included:
 - Django with sqlite database at backend
 - Customized [django_allauth](https://django-allauth.readthedocs.io/en/latest/index.html) app for login/signup flows. Optionally protect login/signup forms with Google ReCAPTCHA
 - React, Bootstrap (optionally Tailwind CSS) at frontend
 - NodeJS and Vite to build frontend and serve it on development
 - [WhiteNoise](http://whitenoise.evans.io/en/stable/) for cache serving (optionally via Nginx on production)
 - Ansible deploy scripts to any server over SSH
   - gunicorn
   - nginx
   - SQLite DB
 - Simple create order application with PayPal payment button integration
 - Several useful Python and JS utils
 - Docker Compose setup with Dockerfiles for local development inside containers
 - Emacs docker integration files
 - Vagratfile to run VM if needed (for testing deployment, etc)

After bootsrtapping a project it creates a default `core` application with homepage containing dummy React component with PayPal pay now button and backend API to handle payment

This is a starting point I use to develop my own projects. Completely opinionated. I use such setup for many years and used to it. It works great for running my projects as a solo developer. This will evolve with time.

## Contribution

Feel free to start a PR, I'm open to any new technology and if it works better then my current setup I would easily adopt it.

## Project Bootstrap

- [ ] Make sure you have Python >= 3.8 installed
- [ ] Install Django with `pip install django`, to have the `django-admin` command available.
- [ ] Open the command line and go to the directory you want to start your project in.
- [ ] Start your project in current directory using (`theprojectname` can only contain alphanumeric chars and underscore):
    ```
    django-admin startproject theprojectname . --extension=py,sh --name=package.json,Dockerfile,hosts.inv,web.yml,docker-compose.yml,.env,Vagrantfile,.dir-locals.el --template=https://github.com/mylh/indiehacker-boilerplate/archive/refs/heads/master.zip
    ```

In the next steps, always remember to replace `theprojectname` with your project's name
- [ ] Above: don't forget the `--extension` and `--name` params!
- [ ] Change the first line of README to the name of the project and update the rest of the file as needed
- [ ] If you use Emacs and docker: escape project path in `docker-pylint.sh` and `run_pylint.sh` let me know if you aware about better way to integrate docker with Emacs


## Running

### Configuring local

- [ ] Adjust settings in `web/backend/theprojectname/settings/base.py` and `web/backend/theprojectname/settings/local.py` and secrets in `web/backend/.env` these are used in local development with docker
- [ ] start development container with `docker-compose up` and apply migrations by running `docker exec -it theprojectname_web python manage.py migrate`
- [ ] create django admin superuser `docker exec -it theprojectname_web python manage.py createsuperuser`
- [ ] go to http://localhost:8000 and check that website is loading

### Starting Docker environment

Then start docker containers with

    docker-compose up

## Deploying to Production

- [ ] Go to `ansible` directory and update `hosts.inv` with IP address and access credentials to your web server
- [ ] Configure vars in `ansible/web.yml`
- [ ] Add entry for `theprojectname-web` host in `~/.ssh/config`
- [ ] set `PROJECT_DOMAIN` in `wev/backend/theprojectname/settings/production` and in `ansible/web.yml`
- [ ] copy `app.env.example` into `app.env` and update values as necessary

Run for full deployment including installation and configuration of all necessary services such as nginx, gunicorn, etc:

    ansible-playbook -i hosts.inv web.yml


Code is deployed from local working copy of the repo. There is an option to deploy from Git. Configure variables in `web.yml`, see `ansible/deploy_django/defaults/main.yml` for details.

### Ansible Variables

Following variables can be defined in web.yml that controls playbook behavior:

- `domain` - make sure to set it to correct domain before deploying, also update it in `settings/base.py`
- `purge_before_install` default False - deletes everything if any from targed directory at web server
- `clear_venv` default False - clears target venv before installation
- `app_user` default `user`. User to be created and used to run website at the webserver
- `deploy_from_local` default True - code is deployed from local working copy
- `deploy_from_git` default False - deploy from Git repository that needs to be additionally configured
- `install_path` on server
- `install_ssl` default False if you need to use your own SSL certificate with nginx, put ssl cerificates into local `/project_dir/ssl` directory
- `nginx_basic_auth` default False - you can restrict access to deployed website, update user and password in `ansible/deploy_django/files/.htaccess` file, default are `appuser:apppassword`
- `nginx_serve_static` and `nginx_serve_media` default False. Set to serve assets via nginx instead of whitenoise
- `install_geoip` default False if you need to install MaxMind GeoIP database
- `apt_install`: list of addtional packages to be installed with apt, default: `redis-server`
- `install_cronjobs`: default False. Change to true and modify necessary cronjobs in `ansible/deploy_django/tasks/cronjobs.yml`

### Tags

Some tags are available to speed up deployment. To make reconfiguration of existing installation

    ansible-playbook -i hosts.inv web.yml -t config


Quick update when only source code changed:

    ansible-playbook -i hosts.inv web.yml -t deploy


### Testing deployment with Vagrant

Run in project dir:

    vagrant up

Configure local ssh access by running

    vagrant ssh-config >> ~/.ssh/config

Uncomment vagrant host in `ansible/hosts.inv`
