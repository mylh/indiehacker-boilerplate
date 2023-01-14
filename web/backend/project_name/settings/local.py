from .base import *  # noqa

DEBUG = True

HOST = "http://localhost:8000"

SECRET_KEY = "secret"

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

AUTH_PASSWORD_VALIDATORS = []  # allow easy passwords only on local

# Email settings for mailhog
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mailhog"
EMAIL_PORT = 1025


JS_REVERSE_JS_MINIFY = False

INTERNAL_IPS = ["172.20.0.1", "127.0.0.1"]

DJANGO_VITE_DEV_MODE = DEBUG
