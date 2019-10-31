from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserInfo(models.Model):
    STATUS1 = (
        (1, '男'),
        (0, '女')
    )
    STATUS2 = (
        (0, '冻结'),
        (1, '活跃')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user1")
    true_name = models.CharField(max_length=255, verbose_name='用户姓名')
    gender = models.IntegerField(choices=STATUS1, verbose_name='用户性别')
    job_number = models.CharField(max_length=255, verbose_name='工号')
    role = models.CharField(max_length=255, verbose_name="角色", null=True, blank=True)
    tel = models.CharField(max_length=255, verbose_name='电话')
    address1 = models.CharField(max_length=255, verbose_name='1级家庭地址')
    address2 = models.CharField(max_length=255, verbose_name='2级家庭地址')
    describe = models.CharField(max_length=255, verbose_name='描述')
    login_update = models.DateTimeField(verbose_name='最近登录时间', null=True, blank=True)
    status = models.IntegerField(choices=STATUS2, default=1, verbose_name="状态")
    picture = models.CharField(max_length=255, verbose_name='用户头像', null=True, blank=True)

# class Role(models.Model):

