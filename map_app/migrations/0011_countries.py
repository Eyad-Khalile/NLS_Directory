# Generated by Django 3.1.6 on 2021-03-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0010_organisation_org_filter_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='country name')),
                ('path', models.CharField(max_length=255, verbose_name='path')),
            ],
        ),
    ]
