# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 07:57
from __future__ import unicode_literals

import ImageOfTheDay.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageOfTheDay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageoftheday',
            name='image',
            field=models.FileField(upload_to=ImageOfTheDay.models.get_upload_file_name),
        ),
    ]
