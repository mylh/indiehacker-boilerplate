import json

from django.views.generic import FormView
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.shortcuts import render
from django.http import Http404
from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from . import applogic
from .billing import EU_VAT
from .forms import SupportForm
from .utils import get_client_ip, get_client_ip_country


def terms(request):
    return render(request, "core/terms.html", {})


def compare(request):
    return render(request, "core/compare.html", {})


class Support(FormView):
    template_name = "core/support.html"
    form_class = SupportForm
    success_url = "/support?success=true"

    def get_context_data(self, **kwargs):
        ctx = super(Support, self).get_context_data()
        ctx["success"] = self.request.GET.get("success")
        ctx["show_form"] = self.request.GET.get("f") == "1"
        return ctx

    def form_valid(self, form):
        reply = form.cleaned_data["reply"]
        if not self.request.user.is_authenticated and not reply:
            form.add_error("reply", "Please provide contact email")
            return self.form_invalid(form)
        form.send_email(
            self.request.user,
            get_client_ip(self.request),
            get_client_ip_country(self.request),
        )
        return super(Support, self).form_valid(form)


def index(request):
    country = get_client_ip_country(request)
    tax_rate = EU_VAT.get(country, 0)
    react_props = {
        "paypal_client_id": settings.PAYPAL_CLIENTID,
        "tax_rate": float(tax_rate),
        "country": country,
        "allow_new_orders": settings.ALLOW_NEW_ORDERS,
    }
    return render(
        request,
        "core/index.html",
        {
            "react_props": json.dumps(react_props),
        },
    )


def order_status(request, sid):
    try:
        order = applogic.get_order(sid)
    except ObjectDoesNotExist:
        raise Http404("Order Invalid")

    react_props = {
        "sessionId": order.guid,
    }
    ctx = {
        "react_props": json.dumps(react_props),
        "order": order,
    }

    return render(request, "core/order_status.html", ctx)


class RestViewSet(viewsets.ViewSet):
    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="rest-check",
    )
    def rest_check(self, request):
        return Response(
            {"result": "If you're seeing this, the REST API is working!"},
            status=status.HTTP_200_OK,
        )
