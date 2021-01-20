# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20170411_0504'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, verbose_name='URL', blank=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('description', models.CharField(max_length=100)),
                ('image', mezzanine.core.fields.FileField(help_text=b'Optional, may be used in certain circumstances and not others', max_length=255, null=True, blank=True)),
                ('href', models.CharField(help_text=b'An optional link for the image or otherwise.', max_length=500, blank=True)),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'db_table': 'mezztend_content_contentblock',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('href', models.CharField(help_text=b'If blank this will simply sit in the menus, otherwise it will link to whatever you specify here.', max_length=500, blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'db_table': 'mezztend_content_menuitem',
                'verbose_name': 'Menu item',
                'verbose_name_plural': 'Menu items',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='TwoColumnRichTextPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('left_column', mezzanine.core.fields.RichTextField(verbose_name='Left column')),
                ('right_column', mezzanine.core.fields.RichTextField(verbose_name='Right column')),
            ],
            options={
                'ordering': ('_order',),
                'db_table': 'mezztend_content_twocolumnrichtextpage',
                'verbose_name': 'Two column rich text page',
                'verbose_name_plural': 'Two column rich text pages',
            },
            bases=('pages.page', models.Model),
        ),
    ]
