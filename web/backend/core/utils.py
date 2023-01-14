import json
from functools import wraps

from django.http import JsonResponse


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_client_ip_country(request):
    return request.META.get("HTTP_CF_IPCOUNTRY", "XX")


def api_error(message, status=400):
    return JsonResponse(
        {"success": False, "message": str(message)}, status=status
    )


def api_success(data=None):
    res = {"success": True, "message": ""}
    if data:
        res.update(data)
    return JsonResponse(res)


def json_request(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if request.method == "POST":
            data = json.loads(request.body)
        elif request.method == "GET":
            data = request.GET
        return view(request, data=data, *args, **kwargs)

    return wrapper
