from django.urls import path

from . import views, views_api


urlpatterns = [
    # Content pages
    path("", views.index, name="index"),
    path("terms/", views.terms, name="terms"),
    path("support/", views.Support.as_view(), name="support"),
    # Main application
    path("order/<uuid:sid>/", views.order_status, name="order_status"),
    # AJAX APIs
    path(
        "api/order/create",
        views_api.create_order,
        name="api_create_order",
    ),
    path(
        "api/session/paypal_payment",
        views_api.paypal_payment,
        name="api_paypal_payment",
    ),
]
