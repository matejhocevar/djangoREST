# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 20:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoRESTApp', '0003_auto_20160112_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
