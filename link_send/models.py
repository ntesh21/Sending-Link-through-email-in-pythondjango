from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Email(models.Model):
	email = models.TextField(max_length=500, blank=True)


@receiver(post_save, sender=User)
def update_user_email(sender, instance, created, **kwargs):
    if created:
        Email.objects.create(user=instance)
    instance.email.save()
   