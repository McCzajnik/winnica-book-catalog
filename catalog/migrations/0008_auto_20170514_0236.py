# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-13 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20170514_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.ManyToManyField(blank=True, help_text='Dodaj tłumaczcza/kę', to='catalog.Translator'),
        ),
    ]
