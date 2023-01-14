from celery.utils.log import get_task_logger
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import mail_admins
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse

from {{ project_name }}.celery import app

logger = get_task_logger(__name__)

@app.task()
def test_celery():
    print("Celery working")
    return True
