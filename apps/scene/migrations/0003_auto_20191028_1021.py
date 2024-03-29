# Generated by Django 2.0 on 2019-10-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scene', '0002_auto_20191025_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarmmanagement',
            name='am_deal_detail',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='处理说明'),
        ),
        migrations.AlterField(
            model_name='alarmmanagement',
            name='am_level_id',
            field=models.IntegerField(choices=[(1, '一般警告'), (2, '严重警告'), (3, '重要警告')], verbose_name='告警等级'),
        ),
        migrations.AlterField(
            model_name='alarmmanagement',
            name='am_status',
            field=models.IntegerField(choices=[(1, '待处理'), (2, '待审核'), (3, '审核通过'), (4, '审核不通过')], verbose_name='处理状态'),
        ),
        migrations.AlterField(
            model_name='alarmmanagement',
            name='am_type_id',
            field=models.IntegerField(choices=[(1, '环境监控'), (2, '消防监控'), (3, '安防监控'), (4, '场景监控')], verbose_name='告警类型'),
        ),
    ]
