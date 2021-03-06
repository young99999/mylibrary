# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_book_pub_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('first_name', models.CharField(max_length=64)),
                ('birth_year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(choices=[(0, 'Unrated'), (1, 'Hate it'), (2, 'Meh'), (3, 'Nice'), (4, 'Loved it'), (5, 'Masterpiece!')], default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.Author'),
        ),
    ]
