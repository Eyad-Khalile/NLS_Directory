# Generated by Django 3.1.6 on 2021-03-13 14:04

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0006_suborganisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suborganisation',
            name='fax',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='fax'),
        ),
        migrations.AlterField(
            model_name='suborganisation',
            name='telephone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='telephone'),
        ),
    ]
