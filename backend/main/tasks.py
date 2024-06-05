from celery import shared_task
from django.conf import settings
from django_email_verification import send_email
from django.contrib.auth import get_user_model
User = get_user_model()

@shared_task
def send_email_confirmation(user_id):
    user = User.objects.get(id=user_id)
    mail_to_sender = send_email(user)
    return mail_to_sender