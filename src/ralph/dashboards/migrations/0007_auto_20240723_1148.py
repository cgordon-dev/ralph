# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2024-07-23 11:48
from __future__ import unicode_literals

from django.db import migrations
from django.core.cache import caches


def clear_sitetree_cache(apps, schema_editor):
    try:
        cache = caches['default']
        cache.delete("sitetrees")
    except Exception as e:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0006_auto_20171221_0959'),
    ]

    operations = [
        migrations.RunPython(
            code=clear_sitetree_cache,
            reverse_code=clear_sitetree_cache
        )
    ]
