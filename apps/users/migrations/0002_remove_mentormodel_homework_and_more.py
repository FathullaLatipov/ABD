# Generated by Django 4.0.4 on 2022-11-18 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentormodel',
            name='homework',
        ),
        migrations.RemoveField(
            model_name='studentsmodel',
            name='homework',
        ),
    ]