# Generated by Django 2.0 on 2018-01-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problems',
            name='profile',
        ),
        migrations.AddField(
            model_name='problems',
            name='ans',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
