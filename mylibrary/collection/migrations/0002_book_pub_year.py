# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pub_year',
            field=models.IntegerField(null=True),
        ),
    ]
