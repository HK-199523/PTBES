import datetime

from django import template
from django.utils import timezone

register = template.Library()


@register.filter(expects_localtime=True)
def is_new(dt: datetime.datetime):
    # newかどうかの基準日
    criteria_date = timezone.now() - datetime.timedelta(days=3)
    return dt >= criteria_date