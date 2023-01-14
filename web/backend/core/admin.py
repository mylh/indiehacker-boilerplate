import csv

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from .models import Order

# from .applogic import start_new_job
# from .tasks import clean_order_data


@admin.register(Order)
class SessionAdmin(admin.ModelAdmin):
    list_display = [
        "guid",
        "created",
        "email",
        "price",
        "paid",
    ]
    search_fields = ["guid", "email", "user_id"]
    # actions = ["start_new_job", "clean_order_data"]
    # inlines = [JobInline, PhotoInline]
    # list_filter = ["is_cleaned"]

    def created(self, obj):
        return obj.created_at.strftime("%d.%m %H:%M")

    # def start_new_job(self, request, queryset):
    #     for session in queryset:
    #         start_new_job(session)
    # start_new_job.short_description = "Start New Processing Job"

    # def clean_order_data(self, request, queryset):
    #     for session in queryset:
    #         clean_session_data.delay(session.guid)
    # clean_session.short_description = "Clean Order Data & Results"
