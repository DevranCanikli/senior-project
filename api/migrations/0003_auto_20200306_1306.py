# Generated by Django 3.0.3 on 2020-03-06 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200303_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='signature',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
