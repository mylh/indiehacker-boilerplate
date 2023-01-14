import json
import logging
import pprint
from decimal import Decimal
import datetime as dt

from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError

from . import applogic
from .utils import get_client_ip_country, api_error, api_success, json_request
from .billing import EU_VAT


log = logging.getLogger(__name__)


@require_POST
@json_request
def create_order(request, data):
    country = get_client_ip_country(request)
    tax_rate = EU_VAT.get(country, 0)

    try:
        order = applogic.create_order(
            email=data["email"],
            tax_rate=tax_rate,
            addon=data.get("addon", False),
        )
        order.newsletter = data.get("newsletter", False)
    except ValidationError as e:
        return api_error(e)
    except Exception as e:
        return api_error(e, status=500)

    return api_success(
        {
            "sid": order.guid,
            "total_price": float(order.price),
        }
    )


@require_POST
def paypal_payment(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        paypal = data["paypal_details"]
        log = logging.getLogger("pay")
        log.debug(
            "PAYMENT RECEIVED:======================================\n%s",
            pprint.pformat(paypal, width=120),
        )
        order = applogic.get_order(data["sid"])
        order.paid = Decimal(paypal["purchase_units"][0]["amount"]["value"])
        order.txn = (
            "paypal:"
            + paypal["purchase_units"][0]["payments"]["captures"][0]["id"]
        )
        order.txn_time = dt.datetime.strptime(
            paypal["purchase_units"][0]["payments"]["captures"][0][
                "update_time"
            ],
            "%Y-%m-%dT%H:%M:%SZ",
        )

        order.save()
        # do other stuff

    except Exception as e:
        return api_error(e)
    return api_success()
