from django.db.models.signals import post_save                                      
from stlonline.settings import EMAIL_HOST_USER
from .models import *
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User


@receiver(post_save, sender = Registration)
def send_email_confirmation(sender, instance, **kwargs):
    password = kwargs.get('pwd')

    if password:
        send_mail(
            subject= 'STL ONLINE REGISTRATION',
            message= 'Thank you for registration in STL ONLINE E-COMMERCE WEBSITE.',
            from_email= EMAIL_HOST_USER,
            recipient_list=[instance.email_id]
         )
        print("Done signal")
        