# Generated by Django 3.1.6 on 2021-03-27 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0015_orgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='org_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Organisations N° / Organisations Nr.'),
        ),
    ]