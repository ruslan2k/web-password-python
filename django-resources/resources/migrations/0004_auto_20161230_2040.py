# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-30 20:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]