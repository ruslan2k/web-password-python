import base64
import os
import random

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salt = models.CharField(max_length=254, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('create_user_profile')
    print(instance)
    if created:
        salt = base64.b64encode(os.urandom(16))
        print('created user, salt {}'.format(salt))
        Profile.objects.create(user=instance, salt=salt)


class Resource(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    key = models.CharField(max_length=250)
    val = models.CharField(max_length=250)
    url = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.key


class Storage(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


