from datetime import datetime
from django.db import models
# Create your models here.
from django.utils import timezone


class Video(models.Model):
    video_name = models.CharField(max_length=255,verbose_name='视频名称')
    video_detail = models.CharField(max_length=255,verbose_name='视频描述')
    video_url = models.CharField(max_length=255,verbose_name='视频地址')
    video_user = models.CharField(max_length=255,verbose_name='视频用户')
    video_passwd = models.CharField(max_length=255,verbose_name='用户密码')
    video_addtime = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

class DoorApprove(models.Model):
    STATUS = (
        (1, '待审核'),
        (2, '已通过'),
        (3, '已拒绝')
    )
    user_id = models.IntegerField(verbose_name='申请人id')
    door_follow = models.CharField(max_length=255,verbose_name='随行人员')
    door_follownum = models.IntegerField(verbose_name='随行人数')
    door_start = models.DateTimeField(verbose_name='申请开始时间')
    door_end = models.DateTimeField(verbose_name='申请结束时间')
    door_addtime = models.DateTimeField(default=timezone.now,verbose_name='申请添加时间')
    door_detail = models.CharField(max_length=255,verbose_name='申请说明')
    door_status = models.CharField(max_length=255,verbose_name='申请状态')
    approve_time = models.DateTimeField(verbose_name='审批时间',null=True,blank=True)
    approve_userid = models.IntegerField(verbose_name='审批人',null=True,blank=True)
    door_feedback = models.CharField(max_length=255,verbose_name='门禁反馈')

class Logs(models.Model):
    user_id = models.IntegerField(verbose_name='用户id')
    scene = models.CharField(max_length=255,verbose_name='场景名')
    log_content = models.CharField(max_length=255,verbose_name='日志内容')
    log_module = models.CharField(max_length=255,verbose_name='所属模块')
    log_addtime = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


