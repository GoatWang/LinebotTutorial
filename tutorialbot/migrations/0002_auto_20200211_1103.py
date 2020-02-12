# Generated by Django 3.0.3 on 2020-02-11 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialbot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='friend',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='promoted',
            field=models.BooleanField(default=False, verbose_name='promoted'),
        ),
    ]
