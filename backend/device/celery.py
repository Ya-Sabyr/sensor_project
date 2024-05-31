import os

from celery import Celery

# from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "device.settings")
app = Celery("device")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()