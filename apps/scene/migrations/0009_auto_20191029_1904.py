# Generated by Django 2.0 on 2019-10-29 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scene', '0008_auto_20191029_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarmlamp',
            name='alarmlamp_name',
            field=models.CharField(default='报警灯', max_length=255),
        ),
        migrations.AddField(
            model_name='alertor',
            name='alertor_name',
            field=models.CharField(default='报警器', max_length=255),
        ),
        migrations.AddField(
            model_name='beam',
            name='beam_name',
            field=models.CharField(default='光照强度传感器', max_length=255),
        ),
        migrations.AddField(
            model_name='display',
            name='display_name',
            field=models.CharField(default='LCD显示器', max_length=255),
        ),
        migrations.AddField(
            model_name='fan',
            name='fan_name',
            field=models.CharField(default='风扇传感器', max_length=255),
        ),
        migrations.AddField(
            model_name='flame',
            name='flame_name',
            field=models.CharField(default='火光传感器', max_length=255),
        ),
        migrations.AddField(
            model_name='humidity',
            name='humidity_name',
            field=models.CharField(default='湿度传感器', max_length=255),
        ),
        migrations.AddField(
            model_name='light',
            name='light_name',
            field=models.CharField(default='灯光传感器', max_length=255),
        ),
        migrations.AddField(
            model_name='pump',
            name='pump_name',
            field=models.CharField(default='水泵表', max_length=255),
        ),
        migrations.AddField(
            model_name='smoke',
            name='smoke_name',
            field=models.CharField(default='烟雾传感器', max_length=255),
        ),
        migrations.AddField(
            model_name='unlocking',
            name='unlocking_name',
            field=models.CharField(default='开锁记录', max_length=255),
        ),
        migrations.AlterField(
            model_name='alarmlamp',
            name='alarmlamp_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 155687), verbose_name='报警灯更新时间'),
        ),
        migrations.AlterField(
            model_name='alertor',
            name='alertor_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 155687), verbose_name='报警器更新时间'),
        ),
        migrations.AlterField(
            model_name='alertor',
            name='alertor_status',
            field=models.IntegerField(choices=[(1, '开'), (2, '关')], verbose_name='报警器状态'),
        ),
        migrations.AlterField(
            model_name='beam',
            name='beam_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 153683), verbose_name='光照更新时间'),
        ),
        migrations.AlterField(
            model_name='co2',
            name='co2_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 154690), verbose_name='co2更新时间'),
        ),
        migrations.AlterField(
            model_name='display',
            name='display_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 155687), verbose_name='显示内容更新时间'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='fan_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 156678), verbose_name='风扇更新时间'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='fan_status',
            field=models.IntegerField(choices=[(1, '开'), (2, '关')], verbose_name='风扇状态'),
        ),
        migrations.AlterField(
            model_name='flame',
            name='flame_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 155687), verbose_name='火光更新时间'),
        ),
        migrations.AlterField(
            model_name='humidity',
            name='humidity_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 153683), verbose_name='湿度更新时间'),
        ),
        migrations.AlterField(
            model_name='invade',
            name='invade_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 157674), verbose_name='入侵检测更新时间'),
        ),
        migrations.AlterField(
            model_name='light',
            name='light_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 156678), verbose_name='灯光数据更新时间'),
        ),
        migrations.AlterField(
            model_name='light',
            name='light_status',
            field=models.IntegerField(choices=[(1, '开'), (2, '关')], verbose_name='灯光状态'),
        ),
        migrations.AlterField(
            model_name='methane',
            name='methane_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 155687), verbose_name='甲烷更新时间'),
        ),
        migrations.AlterField(
            model_name='pm25',
            name='pm25_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 154690), verbose_name='pm25更新时间'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='pump_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 156678), verbose_name='水泵更新时间'),
        ),
        migrations.AlterField(
            model_name='pump',
            name='pump_status',
            field=models.IntegerField(choices=[(1, '开'), (2, '关')], verbose_name='水泵状态'),
        ),
        migrations.AlterField(
            model_name='scene',
            name='scene_addtime',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 157674), verbose_name='场景添加时间'),
        ),
        migrations.AlterField(
            model_name='smoke',
            name='smoke_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 154690), verbose_name='烟雾更新时间'),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='temperature_insert_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 29, 19, 4, 21, 153683), verbose_name='温度更新时间'),
        ),
    ]
