# Generated by Django 3.0.7 on 2020-07-23 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20200723_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='membership',
        ),
    ]