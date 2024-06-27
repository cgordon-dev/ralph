# Generated by Django 2.0.13 on 2024-06-27 15:12

from django.db import migrations
import django.db.models.deletion
import ralph.lib.mixins.fields


class Migration(migrations.Migration):

    dependencies = [
        ('licences', '0010_auto_20240621_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseobjectlicence',
            name='base_object',
            field=ralph.lib.mixins.fields.BaseObjectForeignKey(limit_choices_to=ralph.lib.mixins.fields.BaseObjectForeignKey.limit_choices, on_delete=django.db.models.deletion.CASCADE, related_name='licences', to='assets.BaseObject', verbose_name='Asset'),
        ),
    ]
