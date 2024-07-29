
FROM python:3.10

ENV PYTHONUNBUFFERED 1


# Install system dependencies
RUN apt-get update && \
    apt-get -y --no-install-recommends install \
    gcc \
    build-essential \
    libpq-dev \
    python3 \
    python3-pip \
    python3-dev \
    curl \
    wget \
    sudo

RUN python3 -m pip install --no-cache-dir pip-tools

ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd -g ${GROUP_ID} user && useradd -u ${USER_ID} --create-home --home-dir /home/user -g user user

RUN echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

RUN mkdir -p /home/user/app/web/backend

WORKDIR /home/user/app/web/backend

# install python dependencies
ADD *requirements.in /home/user/app/web/backend/
RUN pip-compile requirements.in > requirements.txt && \
    pip-compile dev-requirements.in > dev-requirements.txt

RUN pip install -r requirements.txt && \
    pip install -r dev-requirements.txt  && \
    pip install psycopg2-binary

ADD web/backend/ /home/user/app/web/backend

# to test with gunicorn
#CMD gunicorn {{ project_name }}.wsgi --log-file - -b 0.0.0.0:8000 --reload

RUN chown -R user:user /home/user/app/web/backend

USER user

# to test with django server
CMD python3 manage.py runserver 0.0.0.0:8000
