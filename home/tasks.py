import time

from celery.app import shared_task
from django.core.mail import send_mail

from home.models import Number


@shared_task
def adding(x, y, num_id):
    time.sleep(10)
    num = Number.objects.get(pk=num_id)
    num.result = x + y
    num.save()
    return num.result


@shared_task
def show():
    send_mail('Celery', 'This is django celery course', 'rezoo@support.com', ['rezam578@gmail.com'])

