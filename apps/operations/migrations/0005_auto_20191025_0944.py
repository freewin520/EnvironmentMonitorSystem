# Generated by Django 2.0 on 2019-10-25 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0004_auto_20191024_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doorapprove',
            name='door_addtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 25, 9, 44, 41, 348883), verbose_name='申请添加时间'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='log_addtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 25, 9, 44, 41, 349882), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_addtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 25, 9, 44, 41, 348883), verbose_name='添加时间'),
        ),
    ]