# Generated by Django 2.0 on 2019-10-29 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scene', '0003_auto_20191028_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarmlamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alarmlamp_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 623695), verbose_name='报警灯更新时间')),
                ('alarmlamp_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='报警灯状态')),
                ('alarmlamp_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Alertor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alertor_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 623695), verbose_name='报警器更新时间')),
                ('alertor_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='报警器状态')),
                ('alertor_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Beam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beam_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 621703), verbose_name='光照更新时间')),
                ('beam_value', models.FloatField(verbose_name='光照强度值')),
                ('beam_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='光照强度状态')),
                ('beam_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Co2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co2_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 622697), verbose_name='co2更新时间')),
                ('co2_value', models.FloatField(verbose_name='co2值')),
                ('co2_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='co2状态')),
                ('co2_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 623695), verbose_name='显示内容更新时间')),
                ('display_content', models.CharField(default='当前无内容', max_length=255, verbose_name='显示内容')),
                ('display_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='设备状态')),
                ('display_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fan_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 624691), verbose_name='风扇更新时间')),
                ('fan_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='风扇状态')),
                ('fan_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Flame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flame_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 622697), verbose_name='火光更新时间')),
                ('flame_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='火光状态')),
                ('flame_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Humidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 621703), verbose_name='湿度更新时间')),
                ('humidity_value', models.FloatField(verbose_name='湿度值')),
                ('humidity_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='传感器状态')),
                ('humidity_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Invade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invade_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 624691), verbose_name='入侵检测更新时间')),
                ('invade_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='入侵状态')),
                ('invade_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 624691), verbose_name='灯光数据更新时间')),
                ('light_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='灯光状态')),
                ('light_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Methane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('methane_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 623695), verbose_name='甲烷更新时间')),
                ('methane_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='甲烷状态')),
                ('methane_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Pm25',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm25_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 622697), verbose_name='pm25更新时间')),
                ('pm25_value', models.FloatField(verbose_name='pm25值')),
                ('pm25_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='pm25状态')),
                ('pm25_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pump_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 624691), verbose_name='水泵更新时间')),
                ('pump_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='水泵状态')),
                ('pump_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Smoke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smoke_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 622697), verbose_name='烟雾更新时间')),
                ('smoke_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='烟雾状态')),
                ('smoke_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature_insert_time', models.DateTimeField(default=datetime.datetime(2019, 10, 29, 10, 7, 14, 621703), verbose_name='温度更新时间')),
                ('temperature_value', models.FloatField(verbose_name='温度值')),
                ('temperature_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='传感器状态')),
                ('temperature_online', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='在线状态')),
            ],
        ),
        migrations.CreateModel(
            name='Unlocking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unlocking_insert_time', models.DateTimeField(verbose_name='开锁记录更新时间')),
                ('user_id', models.IntegerField(verbose_name='开锁用户')),
                ('unlocking_status', models.IntegerField(choices=[(1, '正常'), (2, '异常')], verbose_name='开锁状态')),
                ('unlocking_close', models.DateTimeField(verbose_name='关锁时间')),
            ],
        ),
        migrations.AlterField(
            model_name='alarmmanagement',
            name='am_status',
            field=models.IntegerField(choices=[(1, '待处理'), (2, '待审核'), (3, '审核通过'), (4, '审核不通过')], default=1, verbose_name='处理状态'),
        ),
    ]
