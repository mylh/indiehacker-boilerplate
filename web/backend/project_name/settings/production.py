from decouple import Csv, config

from .base import *  # noqa

PROJECT_DOMAIN = "example.com"
BASE_URL = f"https://{PROJECT_DOMAIN}"

DEBUG = False
FRONTEND_USE_VITE = False
ADMINS = (("Admin", f"support@{PROJECT_DOMAIN}"),)
SECRET_KEY = config("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = [PROJECT_DOMAIN, "localhost"]

STATIC_ROOT = INSTALL_DIR / "staticfiles"
STATIC_URL = "/static/"

MEDIA_ROOT = INSTALL_DIR / "mediafiles"
MEDIA_URL = "/media/"

SERVER_EMAIL = f"root@{PROJECT_DOMAIN}"

# Email settings
EMAIL_HOST = config("EMAIL_HOST", default="localhost")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_USE_TLS = True
EMAIL_PORT = 2587
DEFAULT_FROM_EMAIL = f"noreply@{PROJECT_DOMAIN}"

# Support
SUPPORT_EMAIL = f"support@{PROJECT_DOMAIN}"

# Paypal
PAYPAL_TEST = False

# Security
CSRF_TRUSTED_ORIGINS = [BASE_URL]
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", default=31536000, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True

X_FRAME_OPTIONS = "DENY"

# Redbeat https://redbeat.readthedocs.io/en/latest/config.html#redbeat-redis-url
redbeat_redis_url = config("REDBEAT_REDIS_URL", default="")

# Whitenoise
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

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
            "format": "[{asctime} {module} {levelname}] {message}",
            "style": "{",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "app.log": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": INSTALL_PATH / "logs/django.log",
            "formatter": "verbose",
        },
        "pay": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": INSTALL_PATH / "logs/pay.log",
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "level": "WARNING",
            "handlers": ["app.log"],
        },
        "pay": {
            "handlers": ["pay", "console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["app.log", "console"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

JS_REVERSE_EXCLUDE_NAMESPACES = ["admin"]
