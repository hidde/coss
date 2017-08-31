# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('opensource_clubs', '0006_auto_20170830_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('faq', wagtail.wagtailcore.fields.StreamField((('question', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='General content field, appropriate for questions, titles etc (max 150 chars)', max_length=150)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, default='', help_text='WYSIWYG Editor for general purpose content, (max 1000 chars)', max_length=1000, required=False)), ('link', wagtail.wagtailcore.blocks.URLBlock(help_text='Optional field - accepts a URL (max 200 chars)', max_length=200, required=False)), ('link_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Optional field - Title of the link, (max 100 chars)', max_length=100, required=False))), required=True)),))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
