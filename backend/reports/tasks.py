from celery import shared_task
from django.conf import settings
from django.core.mail import send_mass_mail
from .models import RecordProxy
from sensor.models import Sensor 
from django.contrib.auth import get_user_model
User = get_user_model()

@shared_task
def new_report_notification(report_id):
    report = RecordProxy.objects.get(id=report_id)
    sensor = Sensor.objects.get(id=report.sensor)
    
    message_content = f'Появилась новая запись. \n\nАдрес: {sensor.address}.\nДистанция: {report.distance}'
    from_email = ...
    
    subject = 'Новая запись'
    recipient = User.objects.values_list('email', flat=True)
    
    messages = [(subject, message_content, )]