import uuid
from django.core.validators import validate_email

from .models import Order


def create_order(email, tax_rate=0, addon=False):
    validate_email(email)
    price = 10
    if addon:
        price = price + 10

    order = Order(
        guid=str(uuid.uuid4()),
        email=email,
        price=price,
        tax_rate=tax_rate,
    )
    order.save()

    return order


def get_order(guid):
    order = Order.objects.get(guid=guid)
    return order


def get_order_by_transaction(txn_id, source="apple"):
    key = f"{source}:{txn_id}"
    sessions = Order.objects.filter(txn__istartswith=key)
    return sessions


# def start_new_job(session):
#     if get_current_job(session) is not None:
#         return False

#     from core.tasks import process_session

#     process_session.delay(session.guid)
#     return True
