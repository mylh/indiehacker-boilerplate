from django.db import models


class Order(models.Model):
    guid = models.CharField(max_length=36, blank=False, unique=True)
    email = models.CharField(max_length=255, blank=True)
    newsletter = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    tax_rate = models.SmallIntegerField(default=0)
    paid = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    txn = models.CharField(max_length=255, blank=True)
    txn_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}:{}".format(self.guid, self.email)

    def recalculate_price(self):
        total_price = 10
        return total_price
