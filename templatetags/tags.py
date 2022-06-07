from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag
def current_year(request):
    return datetime.now().date().year