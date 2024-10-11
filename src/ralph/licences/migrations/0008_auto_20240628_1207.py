# Generated by Django 2.0.13 on 2024-06-28 12:07

from django.db import migrations
import django.db.models.deletion
import ralph.lib.mixins.fields


class Migration(migrations.Migration):

    dependencies = [
        ('licences', '0007_auto_20240506_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseobjectlicence',
            name='base_object',
            field=ralph.lib.mixins.fields.BaseObjectForeignKey(limit_models=['back_office.BackOfficeAsset', 'data_center.DataCenterAsset', 'virtual.VirtualServer', 'data_center.Cluster'], on_delete=django.db.models.deletion.CASCADE, related_name='licences', to='assets.BaseObject', verbose_name='Asset'),
        ),
    ]