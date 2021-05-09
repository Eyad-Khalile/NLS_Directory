# Generated by Django 3.1.6 on 2021-04-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0028_auto_20210410_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='full_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Full Address'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Organisation name / Organisationsname'),
        ),
    ]
