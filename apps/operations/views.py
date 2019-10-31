from django.db import connection
from django.db.models import Count, Q
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, mixins, views
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from operations.filters import LogsFilter, DoorApproveFilter, DoorFilter
from operations.schemas import DoolApproveSchema, DoorApproveTimeSchema
from .models import *
import datetime
from .serializers import *

#日志查询
class LogsListView(generics.ListAPIView):
    queryset = Logs.objects.all()  # 查询结果集设置
    serializer_class = LogsFilterSerializers  # 序列器设置
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = LogsFilter
    search_fields = ('log_content',)

    def logsadd(self,user_id,scene,log_content,log_module):
        with connection.cursor() as cursor:
            sql = "INSERT INTO Logs (user_id,scene,log_content,log_module,log_addtime) VALUES (%s,%s,%s,%s);"\
              %(user_id, scene, log_content, log_module, datetime.datetime.now)
            cursor.execute(sql)
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     try:  # 失败信息的定制
    #         serializer.is_valid(raise_exception=True)
    #     except:
    #         return Response(data={'code': 400, 'message': "门禁申请失败",'erro':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     # 成功后返回信息的定制
    #     res = Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
    #     res.data['code'] = 200
    #     res.data['message'] = '门禁申请成功'
    #     return res

#视频查询
class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()  # 查询结果集设置
    serializer_class = VideoListSerializers  # 序列器设置

#视频增加
class VideoAddView(generics.CreateAPIView):
    serializer_class = VideoAddSerializers
    # 自定义返回结果

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:  # 失败信息的定制
            serializer.is_valid(raise_exception=True)
        except:
            return Response(data={'code': 400, 'message': "视频添加失败",'erro':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # 成功后返回信息的定制
        res = Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        res.data['code'] = 200
        res.data['message'] = '视频添加成功'
        return res

#视频删除
class VideoDelView(generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoListSerializers
    #重写destroy方法自定义返回结果
    def get(self,request,pks):
        pks = pks.split(",")
        for pk in pks:
            pk = int(pk)
            # 获取地址url中的参数
            try:
                # 使用get获取单条数据
                Video.objects.get(pk=pk).delete()
            except:
                return Response(data={'code': 400, 'message': '删除失败'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code':200,'message':'删除成功'},status=status.HTTP_200_OK)

# 视频更新
class VideoUpdView(generics.GenericAPIView,mixins.UpdateModelMixin):
    queryset = Video.objects.all()
    serializer_class = VideoAddSerializers
    def post(self,request,*args,**kwargs):
        # print('request:',request)
        # print(kwargs)
        # 调用UpdateModelMixin中的update方法
        try:
            self.update(request,*args,**kwargs)
        except:
            return Response(data={'code':400,'message':'修改失败'},status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code':200,'message':'修改成功'},status=status.HTTP_200_OK)

#门禁查询
class DoorApproveView(generics.ListAPIView):
    queryset = DoorApprove.objects.all()  # 查询结果集设置
    serializer_class = DoorApproveSerializers  # 序列器设置
    filterset_class = DoorApproveFilter

#门禁添加
class DoorApproveAddView(generics.CreateAPIView):
    serializer_class = DoorApproveAddSerializers
    # 自定义返回结果

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:  # 失败信息的定制
            serializer.is_valid(raise_exception=True)
        except:
            return Response(data={'code': 400, 'message': "门禁申请失败",'erro':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # 成功后返回信息的定制
        res = Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        res.data['code'] = 200
        res.data['message'] = '门禁申请成功'
        return res

#门禁更新
class DoorApproveUpdView(generics.GenericAPIView,mixins.UpdateModelMixin):
    queryset = DoorApprove.objects.all()
    serializer_class = DoorApproveUpdSerializers
    schema = DoolApproveSchema

    def post(self,request,*args,**kwargs):
        try:
            id = self.request.query_params.get('door_id', '')
            # 审核标志
            feedback = request.data.get("door_feedback")
            door_status = request.data.get("door_status")
            access = DoorApprove.objects.get(pk=id)
            # 审批时间
            access.door_feedback = feedback
            access.door_status = door_status
            access.approve_time = datetime.now()
            access.approve_userid = '1'
            access.save()

        except:
            return Response(data={'code':400,'message':'修改失败'},status=status.HTTP_400_BAD_REQUEST,)
        return Response(data={'code':200,'message':'修改成功'},status=status.HTTP_200_OK)

class DoorApproveNumView(views.APIView):
    # queryset = DoorApprove.objects.all()  # 查询结果集设置
    # serializer_class = DoorApproveSerializers  # 序列器设置
    # # filter_backends = (DjangoFilterBackend, SearchFilter)
    # filterset_class = DoorFilter
    # filterset_class = DoorFilter
    schema = DoorApproveTimeSchema
    def get(self, request):
        time_min = self.request.query_params.get('time_min', '')
        time_max = self.request.query_params.get('time_max', '')
        time_min = datetime.strptime(time_min, "%Y-%m-%d %H:%M:%S")
        time_max = datetime.strptime(time_max, "%Y-%m-%d %H:%M:%S")
        query_object = DoorApprove.objects.values("user_id").filter(Q(door_addtime__lte=time_max)&Q(door_addtime__gte=time_min)).annotate(count=Count("user_id"))
        total = 0
        for obj in query_object:
            total += obj['count']
        for obj in query_object:
            obj["count"] = obj["count"]/total
        return Response(data=query_object)


class DoortimesumView(views.APIView):
    schema = DoorApproveTimeSchema
    def get(self,request):
        time_min = self.request.query_params.get('time_min', '')
        time_max = self.request.query_params.get('time_max', '')
        time_min = datetime.strptime(time_min, "%Y-%m-%d %H:%M:%S")
        time_max = datetime.strptime(time_max, "%Y-%m-%d %H:%M:%S")
        print(time_min,time_max)
        with connection.cursor() as cursor:
            sql = "select user_id,sum(timestampdiff(second, door_start, door_end)) as sumtime " \
                  "from operations_doorapprove " \
                  "where door_start >= '{}' and door_start <= '{}' " \
                  "group by user_id;".format(time_min, time_max)
            cursor.execute(sql)
            row = cursor.fetchall()
            total = 0
            doortime_sumdict = {}
            for obj in row:
                total += obj[1]

            for obj in row:
                doortime_sumdict[obj[0]] = obj[1]/total
                # doortime_sumdict[obj[0]] = obj[1]
                # doortime_sumdict[total]
                # total += obj['count']
        return Response(data=doortime_sumdict)