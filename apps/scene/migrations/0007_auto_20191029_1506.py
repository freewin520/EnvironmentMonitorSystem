# Generated by Django 2.0 on 2019-10-29 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scene', '0006_auto_20191029_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarmlamp',
            name='alarmlamp_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 73096), verbose_name='报警灯更新时间'),
        ),
        migrations.AlterField(
            model_name='alertor',
            name='alertor_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 73096), verbose_name='报警器更新时间'),
        ),
        migrations.AlterField(
            model_name='beam',
            name='beam_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 69107), verbose_name='光照更新时间'),
        ),
        migrations.AlterField(
            model_name='co2',
            name='co2_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 70190), verbose_name='co2更新时间'),
        ),
        migrations.AlterField(
            model_name='display',
            name='display_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 74476), verbose_name='显示内容更新时间'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='fan_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 77121), verbose_name='风扇更新时间'),
        ),
        migrations.AlterField(
            model_name='flame',
            name='flame_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 72098), verbose_name='火光更新时间'),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='humidity_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 67168), verbose_name='湿度更新时间'),
        ),
        migrations.AlterField(
            model_name='invade',
            name='invade_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 79116), verbose_name='入侵检测更新时间'),
        ),
        migrations.AlterField(
            model_name='light',
            name='light_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 75136), verbose_name='灯光数据更新时间'),
        ),
        migrations.AlterField(
            model_name='methane',
            name='methane_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 72098), verbose_name='甲烷更新时间'),
        ),
        migrations.AlterField(
            model_name='pm25',
            name='pm25_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 70190), verbose_name='pm25更新时间'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='pump_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 76125), verbose_name='水泵更新时间'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_addtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 80113), verbose_name='场景添加时间'),
        ),
        migrations.AlterField(
            model_name='smoke',
            name='smoke_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 71101), verbose_name='烟雾更新时间'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='temperature_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 15, 6, 20, 68113), verbose_name='温度更新时间'),
        ),
    ]
