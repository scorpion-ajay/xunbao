# Generated by Django 2.0 on 2018-01-12 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20180112_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['solved', 'timetaken']},
        ),
        migrations.AddField(
            model_name='profile',
            name='timetaken',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
