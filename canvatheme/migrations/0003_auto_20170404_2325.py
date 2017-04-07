# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvatheme', '0002_auto_20170404_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='heading_link',
            field=models.CharField(blank=True, help_text='Optional, if provided will redirect to this link', max_length=2000),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='heading',
            field=models.CharField(blank=True, help_text='Call on action text', max_length=200),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subheading',
            field=models.CharField(help_text='Call on action button', max_length=200),
        ),
    ]