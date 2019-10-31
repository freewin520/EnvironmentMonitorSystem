from rest_framework import serializers

from scene.models import *
from users.models import UserInfo


class AlarmListSerializers(serializers.ModelSerializer):
    # user = UserSerializers()
    class Meta:
        model = AlarmManagement
        fields = ('am_addtime', 'am_type_id', 'am_level_id', 'scene_id', 'am_device', 'am_content', 'am_status')


class AlarmViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = AlarmManagement
        fields = "__all__"


# 场景序列化器
class SceneSerializers(serializers.ModelSerializer):
    # # 隐藏user字段,并且赋值为当前登录用户
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )

    class Meta:
        model = Scene
        exclude = ("scene_gatewaypwd","scene_level")


# 场景添加序列化器
class SceneAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ("scene_name", "scene_code", "scene_gatewaypwd", "scene_level")

