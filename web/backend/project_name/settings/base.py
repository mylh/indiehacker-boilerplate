# https://docs.djangoproject.com/en/1.10/ref/settings/
from decouple import config  # noqa
from dj_database_url import parse as db_url  # noqa
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
INSTALL_DIR = BASE_DIR.parent.parent

BASE_URL = "http://localhost:8000"

SITE_ID = 1

DEBUG = True
FRONTEND_USE_VITE = True

ADMINS = (("Admin", "ubuntu@localhost"),)
DEFAULT_FROM_EMAIL = "noreply@localhost"
SUPPORT_EMAIL = "support@localhost"

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": config("DATABASE_URL", cast=db_url),
}

DATABASES["default"]["ATOMIC_REQUESTS"] = True


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django_js_reverse",
    "django_vite",
    "rest_framework",
    "crispy_forms",
    "crispy_bootstrap5",
    # django_allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # project apps
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # django-allauth
    "allauth.account.middleware.AccountMiddleware",
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

ROOT_URLCONF = "{{ project_name }}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.global_context",
            ],
        },
    },
]

WSGI_APPLICATION = "{{ project_name }}.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

# vite config
DJANGO_VITE_ASSETS_PATH = BASE_DIR / ".." / "frontend" / "dist"
DJANGO_VITE_DEV_MODE = False
VITE_SERVER_URL = "http://localhost:3000"

STATICFILES_DIRS = (
    BASE_DIR / ".." / "frontend" / "assets",
    DJANGO_VITE_ASSETS_PATH,
)

STATIC_ROOT = INSTALL_DIR / "staticfiles"

MEDIA_ROOT = INSTALL_DIR / "mediafiles"
MEDIA_URL = "/media/"


# Celery
# Celery
CELERY_BROKER_URL = config("CELERY_BROKER_URL")
# CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND")
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
# CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_TIMEZONE = TIME_ZONE

# # Sentry
# SENTRY_DSN = config("SENTRY_DSN", default="")
# COMMIT_SHA = config("HEROKU_SLUG_COMMIT", default="")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Workaround for django_js_reverse
import django
from django.utils.encoding import force_str

django.utils.encoding.force_text = force_str

# Crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# allauth
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
SOCIALACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = "/app/"

# Uncomment this if you want to protect login and signup forms with reCAPTCHA
INSTALLED_APPS += ["django_recaptcha"]
ACCOUNT_FORMS = {
    "login": "core.forms.InvisibleRecaptchaLoginForm",
    "signup": "core.forms.InvisibleRecaptchaSignupForm",
}
RECAPTCHA_PRIVATE_KEY = config("RECAPTCHA_PRIVATE_KEY")
RECAPTCHA_PUBLIC_KEY = config("RECAPTCHA_PUBLIC_KEY")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "verbose": {
            "format": "[{asctime}] {module} {levelname} : {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
        "message": {
            "format": "%(asctime)s %(message)s",
        },
    },
    "handlers": {
        "request.file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/tmp/django.log",
            "formatter": "verbose",
        },
        "pay": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/tmp/pay.log",
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
        "pay": {
            "handlers": ["pay", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["request.file", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
        # 'django.db.backends': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        # }
    },
}

# PAYPAL
PAYPAL_TEST = True
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"
PAYPAL_BUSINESS_ACCONT = config("PAYPAL_BUSINESS_ACCONT")
PAYPAL_CLIENTID = config("PAYPAL_CLIENTID")
PAYPAL_SECRET = config("PAYPAL_SECRET")

ALLOW_NEW_ORDERS = True
