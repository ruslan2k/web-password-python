# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-06 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_resource_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='url',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
