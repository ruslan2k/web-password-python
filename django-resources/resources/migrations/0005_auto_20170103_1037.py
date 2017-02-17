# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-03 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('resources', '0004_auto_20161230_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='user',
        ),
        migrations.AddField(
            model_name='resource',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
            preserve_default=False,
        ),
    ]
