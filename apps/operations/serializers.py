# *_*coding:utf-8 *_*
#隐藏user字段,并且赋值为当前登录用户
from rest_framework import serializers

from .models import *
class LogsFilterSerializers(serializers.ModelSerializer):
    # #隐藏user字段,并且赋值为当前登录用户
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )
    class Meta:
        model = Logs
        # fields = ('log_addtime','log_module','log_content','scene')#包含
        exclude = ("user_id",)
        extra_kwargs = {  # 对模型已有参数重新
            'log_addtime': {'required': False, 'read_only': True},
            'log_module': {'required': False, 'read_only': True},
            'log_content': {'required': False, 'read_only': True},
            'scene': {'required': False, 'read_only': True}
        }

class VideoListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ("video_name","video_detail",)


class VideoAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ("id", "video_addtime",)
 

class DoorApproveSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoorApprove
        exclude = ("door_addtime",)

class DoorApproveAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoorApprove
        fields=("user_id","door_start","door_end","door_follow","door_follownum","door_detail")
        extra_kwargs = {  # 对模型已有参数重新
            'door_addtime': {'required': False, 'read_only': True},
            'door_status': {'required': False, 'read_only': True},
            'approve_userid': {'required': False, 'read_only': True},
            'door_feedback': {'required': False, 'read_only': True},
            'approve_time': {'required': False, 'read_only': True},
        }

class DoorApproveUpdSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoorApprove
        fields=("door_status","door_feedback",)