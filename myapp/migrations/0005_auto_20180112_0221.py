# Generated by Django 2.0 on 2018-01-11 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
