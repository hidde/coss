# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-09 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import networkapi.people.models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20170307_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternetHealthIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='affiliations',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='person',
            name='partnership_logo',
            field=models.ImageField(default='images/shared/default.png', max_length=2048, upload_to=networkapi.people.models.get_people_partnership_logo_upload_path),
        ),
        migrations.AddField(
            model_name='person',
            name='quote',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(default='images/shared/default.png', max_length=2048, upload_to=networkapi.people.models.get_people_image_upload_path),
        ),
        migrations.AddField(
            model_name='person',
            name='internetHealthIssues',
            field=models.ManyToManyField(related_name='people', to='people.InternetHealthIssue'),
        ),
    ]
