from datetime import datetime
from django.db import models
# Create your models here.
from django.utils import timezone


class AlarmManagement(models.Model):
    STATUS = (
        (1, '环境监控'),
        (2, '消防监控'),
        (3, '安防监控'),
        (4, '场景监控')
    )
    STATUS2 = (
        (1, '一般警告'),
        (2, '严重警告'),
        (3, '重要警告')
    )
    STATUS3 = (
        (1, '待处理'),
        (2, '待审核'),
        (3, '审核通过'),
        (4, '审核不通过')
    )
    am_addtime = models.DateTimeField(default=datetime.now, verbose_name='告警时间')
    am_type_id = models.IntegerField(choices=STATUS, verbose_name='告警类型')
    am_level_id = models.IntegerField(choices=STATUS2, verbose_name='告警等级')
    scene_id = models.IntegerField(verbose_name='告警场景id')
    am_device = models.CharField(max_length=255, verbose_name='告警设备')
    am_content = models.CharField(max_length=255, verbose_name='告警内容')
    am_status = models.IntegerField(choices=STATUS3, default=1, verbose_name='处理状态')
    am_deal_user = models.CharField(max_length=255, verbose_name="告警处理人", null=True, blank=True)
    am_deal_time = models.DateTimeField(verbose_name='处理时间', null=True, blank=True)
    am_deal_detail = models.CharField(max_length=255, verbose_name='处理说明', null=True, blank=True)
    am_audit_user = models.CharField(max_length=255, verbose_name='告警审核人', null=True, blank=True)
    am_audit_time = models.DateTimeField(verbose_name='审核时间', null=True, blank=True)
    am_audit_feedback = models.CharField(max_length=255,verbose_name='审核反馈', null=True, blank=True)


# 湿度传感器
class Humidity(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    humidity_name = models.CharField(max_length=255, default='湿度传感器')
    humidity_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='湿度更新时间')
    humidity_value = models.FloatField(verbose_name='湿度值')
    humidity_status = models.IntegerField(choices=STATUS1, verbose_name='传感器状态')
    humidity_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "湿度传感器"


# 温度传感器
class Temperature(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    temperature_name = models.CharField(max_length=255, default='温度传感器')
    temperature_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='温度更新时间')
    temperature_value = models.FloatField(verbose_name='温度值')
    temperature_status = models.IntegerField(choices=STATUS1, verbose_name='传感器状态')
    temperature_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "温度传感器"


# 光照强度传感器
class Beam(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    beam_name = models.CharField(max_length=255, default='光照强度传感器')
    beam_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='光照更新时间')
    beam_value = models.FloatField(verbose_name='光照强度值')
    beam_status = models.IntegerField(choices=STATUS1, verbose_name='光照强度状态')
    beam_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "光照强度传感器"


# 二氧化碳传感器
class Co2(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    co2_name = models.CharField(max_length=255, default='CO2传感器')
    co2_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='co2更新时间')
    co2_value = models.FloatField(verbose_name='co2值')
    co2_status = models.IntegerField(choices=STATUS1, verbose_name='co2状态')
    co2_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "二氧化碳传感器"


# PM2.5传感器
class Pm25(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    pm25_name = models.CharField(max_length=255, default='PM2.5传感器')
    pm25_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='pm25更新时间')
    pm25_value = models.FloatField(verbose_name='pm25值')
    pm25_status = models.IntegerField(choices=STATUS1, verbose_name='pm25状态')
    pm25_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "PM2.5传感器"


# 烟雾传感器
class Smoke(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    smoke_name = models.CharField(max_length=255, default="烟雾传感器")
    smoke_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='烟雾更新时间')
    smoke_status = models.IntegerField(choices=STATUS1, verbose_name='烟雾状态')
    smoke_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "烟雾传感器"


# 火光传感器
class Flame(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    flame_name = models.CharField(max_length=255, default="火光传感器")
    flame_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='火光更新时间')
    flame_status = models.IntegerField(choices=STATUS1, verbose_name='火光状态')
    flame_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "火光传感器"


# 甲烷传感器
class Methane(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    methane_name = models.CharField(max_length=255, default='甲烷传感器')
    methane_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='甲烷更新时间')
    methane_status = models.IntegerField(choices=STATUS1, verbose_name='甲烷状态')
    methane_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "甲烷传感器"


# 报警灯
class Alarmlamp(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    alarmlamp_name = models.CharField(max_length=255, default="报警灯")
    alarmlamp_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='报警灯更新时间')
    alarmlamp_status = models.IntegerField(choices=STATUS1, verbose_name='报警灯状态')
    alarmlamp_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "报警灯"


# 报警器
class Alertor(models.Model):
    STATUS1 = (
        (1, '开'),
        (2, '关')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    alertor_name = models.CharField(max_length=255, default="报警器")
    alertor_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='报警器更新时间')
    alertor_status = models.IntegerField(choices=STATUS1, verbose_name='报警器状态')
    alertor_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "报警器"


# LCD显示器
class Display(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    display_name = models.CharField(max_length=255, default="LCD显示器")
    display_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='显示内容更新时间')
    display_content = models.CharField(max_length=255, default="当前无内容", verbose_name='显示内容')
    display_status = models.IntegerField(choices=STATUS1, verbose_name='设备状态')
    display_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "LCD显示器"

# 灯光传感器
class Light(models.Model):
    STATUS1 = (
        (1, '开'),
        (2, '关')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    light_name = models.CharField(max_length=255, default="灯光传感器")
    light_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='灯光数据更新时间')
    light_status = models.IntegerField(choices=STATUS1, verbose_name='灯光状态')
    light_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "灯光传感器"

# 水泵表
class Pump(models.Model):
    STATUS1 = (
        (1, '开'),
        (2, '关')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    pump_name = models.CharField(max_length=255, default="水泵表")
    pump_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='水泵更新时间')
    pump_status = models.IntegerField(choices=STATUS1, verbose_name='水泵状态')
    pump_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "水泵传感器"


# 风扇传感器
class Fan(models.Model):
    STATUS1 = (
        (1, '开'),
        (2, '关')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    fan_name = models.CharField(max_length=255, default="风扇传感器")
    fan_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='风扇更新时间')
    fan_status = models.IntegerField(choices=STATUS1, verbose_name='风扇状态')
    fan_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "风扇传感器"


# 开锁记录表
class Unlocking(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    unlocking_name = models.CharField(max_length=255, default="开锁记录")
    unlocking_insert_time = models.DateTimeField(verbose_name='开锁记录更新时间')
    user_id = models.IntegerField(verbose_name="开锁用户")
    unlocking_status = models.IntegerField(choices=STATUS1, verbose_name='开锁状态')
    unlocking_close = models.DateTimeField(verbose_name='关锁时间')

    class Meta:
        verbose_name = "开锁记录表"


# 入侵检测
class Invade(models.Model):
    STATUS1 = (
        (1, '正常'),
        (2, '异常')
    )
    STATUS2 = (
        (1, '在线'),
        (2, '离线')
    )
    invade_name = models.CharField(max_length=255, default='门禁')
    invade_insert_time = models.DateTimeField(default=datetime.now(), verbose_name='入侵检测更新时间')
    invade_status = models.IntegerField(choices=STATUS1, verbose_name='入侵状态')
    invade_online = models.IntegerField(choices=STATUS2, verbose_name='在线状态')

    class Meta:
        verbose_name = "入侵检测"

# 场景表
class Scene(models.Model):
    STATUS = (
        (1, '在线'),
        (2, '离线')
    )
    scene_addtime = models.DateTimeField(default=datetime.now(), verbose_name='场景添加时间')
    scene_name = models.CharField(max_length=255, verbose_name='场景名称')
    scene_code = models.CharField(max_length=255, verbose_name='场景识别码')
    scene_gatewaypwd = models.CharField(max_length=255, verbose_name='网关密码')
    scene_status = models.IntegerField(choices=STATUS, default=2, verbose_name='场景状态')
    scene_level = models.IntegerField(verbose_name='场景优先级')
