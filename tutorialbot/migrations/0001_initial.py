# Generated by Django 3.0.3 on 2020-02-10 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('line_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='LineID')),
                ('line_name', models.CharField(max_length=100, verbose_name='Line名稱')),
                ('line_picture_url', models.URLField(verbose_name='Line照片網址')),
                ('line_status_message', models.CharField(blank=True, max_length=100, null=True, verbose_name='Line狀態訊息')),
                ('unfollow', models.BooleanField(default=False, verbose_name='封鎖')),
                ('friend', models.BooleanField(default=True, verbose_name='好友')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='創建時間')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
