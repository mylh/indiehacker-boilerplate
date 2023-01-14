from django.conf import settings


def global_context(request):

    ctx = {
        "VITE_SERVER_URL": settings.VITE_SERVER_URL,
        "BASE_URL": settings.BASE_URL,
        "FRONTEND_USE_VITE": settings.FRONTEND_USE_VITE,
    }
    return ctx
