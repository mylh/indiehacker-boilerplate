import logging
from decimal import Decimal

import requests
from django.conf import settings


logger = logging.getLogger(__name__)


def _ep(method):
    if settings.PAYPAL_TEST:
        hostname = "https://api.sandbox.paypal.com"
    else:
        hostname = "https://api.paypal.com"
    return hostname + method


def get_auth():
    session = requests.Session()
    session.auth = (settings.PAYPAL_CLIENTID, settings.PAYPAL_SECRET)

    res = session.post(
        _ep("/v1/oauth2/token"),
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "client_credentials",
        },
    )
    res.raise_for_status()

    auth = res.json()
    return auth


def verify_payment(order_id, amount):
    auth = get_auth()
    res = requests.get(
        _ep("/v2/payments/captures/" + order_id),
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + auth["access_token"],
        },
    )

    if res.status_code != 200:
        return False

    details = res.json()

    if (
        details["amount"]["currency_code"] != "USD"
        or Decimal(details["amount"]["value"]) != amount
    ):
        return False

    return True
