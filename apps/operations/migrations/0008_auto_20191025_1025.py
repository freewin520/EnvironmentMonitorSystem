# Generated by Django 2.0 on 2019-10-25 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0007_auto_20191025_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doorapprove',
            name='door_addtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 25, 10, 25, 37, 283100), verbose_name='申请添加时间'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='log_addtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 25, 10, 25, 37, 284097), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_addtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 25, 10, 25, 37, 282102), verbose_name='添加时间'),
        ),
    ]