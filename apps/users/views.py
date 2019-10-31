from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, views, mixins
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from users.schemas import UserAddSchema
from .serializers import UserSerializers, UserUpdSerializers
from .models import *
User = get_user_model()


# 用户信息列表=
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('username',)


# 用户新增
class UserAddView(views.APIView):

    schema = UserAddSchema

    # 自定义返回结果
    def post(self,requser):
        username = self.request.data.get('username', '')
        password = self.request.data.get('password', '')
        true_name = self.request.data.get('true_name', '')
        tel = self.request.data.get('tel', '')
        gender = self.request.data.get('gender', '')
        status1 = self.request.data.get('status', '')
        job_number = self.request.data.get('job_number', '')
        address1 = self.request.data.get('address1', '')
        address2 = self.request.data.get('address2', '')
        describe = self.request.data.get('describe', '')
        picture = self.request.data.get('picture', '')



        try:
            # 失败信息的定制
            user = User(username=username,password=password)
            user.save()
            userinfo = UserInfo(true_name=true_name,tel=tel,gender=gender,status=status1,job_number=job_number,address1=address1,
                                address2=address2,describe=describe,picture=picture,user_id=user.id)
            userinfo.save()

        except Exception as e:
            print(e)
            return Response(data={'code': 400, 'message': "用户添加失败"},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 400, 'message': "用户添加成功"},
                        status=status.HTTP_400_BAD_REQUEST)


# 用户删除
class UserDeleteView(views.APIView):
    queryset = User.objects.all()

    # 重写destroy方法自定义返回结果
    def get(self, request, pk):
            # 获取地址url中的参数
            try:
                # 使用get获取单条数据
                UserInfo.objects.get(user_id=pk).delete()
                User.objects.get(pk=pk).delete()
            except Exception as e:
                print(e)
                return Response(data={'code': 400, 'message': '删除失败'}, status=status.HTTP_400_BAD_REQUEST)
            return Response(data={'code': 200, 'message': '删除成功'}, status=status.HTTP_200_OK)


# 用户更新
class UserUpdView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = UserInfo.objects.all()
    serializer_class = UserUpdSerializers

    def post(self, request, *args, **kwargs):
        try:
            self.update(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return Response(data={'code': 400, 'message': '修改失败'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 200, 'message': '修改成功'}, status=status.HTTP_200_OK)
