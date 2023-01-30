from django import template

register = template.Library()


@register.filter
def yesno(value):
    return "Yes" if value else "No"