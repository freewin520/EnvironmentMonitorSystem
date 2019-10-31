from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import UserInfo
User = get_user_model()


class UserInfoListSerializers(serializers.ModelSerializer):
    # user = UserSerializers()
    class Meta:
        model = UserInfo
        fields = "__all__"    # 全部列


class UserSerializers(serializers.ModelSerializer):
    user1 = UserInfoListSerializers(many=True)

    class Meta:
        model = User
        fields = "__all__"    # 全部列


class UserUpdSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ("true_name","tel","gender","status","address1","address2","describe","picture")    # 全部列
