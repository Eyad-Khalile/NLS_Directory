# Generated by Django 3.1.6 on 2021-03-14 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0008_auto_20210314_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suborganisation',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_orgs_list', to='map_app.organisation', verbose_name='Organisation name'),
        ),
    ]
