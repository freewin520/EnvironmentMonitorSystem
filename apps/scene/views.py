from django.db import connection
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, views, mixins
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from datetime import datetime
from django.contrib.auth.models import User

from scene.filters import AlarmFilter
from scene.models import *
from scene.schemas import *
from scene.serializers import AlarmListSerializers, AlarmViewSerializers, SceneSerializers, SceneAddSerializers


# 警告过滤
class AlarmListView(generics.ListAPIView):
    queryset = AlarmManagement.objects.all()
    serializer_class = AlarmListSerializers
    filterset_class = AlarmFilter

# 批量处理
class AlarmBatchProcessView(views.APIView):
    schema = AlarmListSchema
    def post(self,request,*args,**kwargs):
        try:
            # 审核标志
            am_type_id = request.data.get("am_type_id")
            am_deal_detail = request.data.get("am_deal_detail")
            access = AlarmManagement.objects.get(am_type_id=am_type_id,am_status=1)
            # 审批时间
            access.am_status = 2
            access.am_deal_time = datetime.now()
            access.am_deal_detail = am_deal_detail
            access.save()
            with connection.cursor() as cursor:
                sql = """
                    select am_type_id,count(*)
                    from scene_alarmmanagement
                    group by am_type_id;
                    """
                cursor.execute(sql)
                row = cursor.fetchall()
        except:
            return Response(data={'code':400,'message':'修改失败'},status=status.HTTP_400_BAD_REQUEST,)
        return Response(data={'code':200,'message':'修改成功','number':row},status=status.HTTP_200_OK)


# 批量审核
class AlarmBatchCheckView(views.APIView):
    schema = AlarmBatchCheckSchema

    def post(self, request, *args, **kwargs):
        try:
            # 审核标志
            am_type_id = request.data.get("am_type_id")
            am_audit_feedback = request.data.get("am_audit_feedback")
            am_status = request.data.get("am_status")
            access = AlarmManagement.objects.get(am_type_id=am_type_id, am_status=2)
            # 审批时间
            access.am_status = am_status
            access.am_deal_time = datetime.now()
            access.am_audit_feedback = am_audit_feedback
            access.save()
            with connection.cursor() as cursor:
                sql = """
                        select am_type_id,count(*)
                        from scene_alarmmanagement
                        group by am_type_id;
                        """
                cursor.execute(sql)
                row = cursor.fetchall()
        except:
            return Response(data={'code': 400, 'message': '修改失败'}, status=status.HTTP_400_BAD_REQUEST, )
        return Response(data={'code': 200, 'message': '修改成功', 'number': row}, status=status.HTTP_200_OK)

# 单行处理
class AlarmProcessView(views.APIView):
    schema = AlarmProcessSchema

    def post(self,request,*args,**kwargs):
        try:
            id = self.request.data.get('am_id')
            am_deal_detail = self.request.data.get('am_deal_detail')
            access = AlarmManagement.objects.get(pk=id)
            access.am_status = 2
            access.am_deal_time = datetime.now()
            access.am_deal_detail = am_deal_detail
            access.save()

        except:
            return Response(data={'code':400,'message':'修改失败'},status=status.HTTP_400_BAD_REQUEST,)
        return Response(data={'code':200,'message':'修改成功'},status=status.HTTP_200_OK)


# 单行审核
class AlarmCheckView(views.APIView):
    schema = AlarmCheckSchema

    def post(self,request,*args,**kwargs):
        try:
            id = self.request.data.get('am_id')
            am_audit_feedback = self.request.data.get('am_audit_feedback')
            am_status = self.request.data.get('am_status')
            access = AlarmManagement.objects.get(pk=id)
            access.am_status = am_status
            access.am_deal_time = datetime.now()
            access.am_audit_feedback = am_audit_feedback
            access.save()
        except:
            return Response(data={'code':400,'message':'修改失败'},status=status.HTTP_400_BAD_REQUEST,)
        return Response(data={'code':200,'message':'修改成功'},status=status.HTTP_200_OK)


# 警告查看
class AlarmView(generics.RetrieveAPIView):
    queryset = AlarmManagement.objects.all()
    # queryset = Favor.objects.filter(user=request.user)error
    serializer_class = AlarmViewSerializers


# 告警的数量统计
class AlarmNum1StaticView(views.APIView):
    schema = AlarmNumStaticSchema

    def get(self,request):
        time_min = self.request.query_params.get('time_min', '')
        time_max = self.request.query_params.get('time_max', '')
        time_min = datetime.strptime(time_min, "%Y-%m-%d %H:%M:%S")
        time_max = datetime.strptime(time_max, "%Y-%m-%d %H:%M:%S")
        with connection.cursor() as cursor:
            sql = """select am_type_id, count(*)
                        from scene_alarmmanagement
                        where am_addtime>='{}' and am_addtime<='{}'
                        GROUP BY am_type_id""".format(time_min,time_max)
            cursor.execute(sql)
            row = cursor.fetchall()
            total = 0
            doortime_sumdict = {}
            for obj in row:
                total += obj[1]
            for obj in row:
                doortime_sumdict[obj[0]] = obj[1]/total
        return Response(data=doortime_sumdict)


# 告警的数量统计
class AlarmNum2StaticView(views.APIView):
    schema = AlarmNumStaticSchema
    def get(self,request,type):
        time_min = self.request.query_params.get('time_min', '')
        time_max = self.request.query_params.get('time_max', '')
        time_min = datetime.strptime(time_min, "%Y-%m-%d %H:%M:%S")
        time_max = datetime.strptime(time_max, "%Y-%m-%d %H:%M:%S")
        with connection.cursor() as cursor:
            sql = """select am_status, count(*)
                        from scene_alarmmanagement
                        where am_addtime>='{}' and am_addtime<='{}' and am_type_id='{}'
                        GROUP BY am_status
                            having am_status != 1""".format(time_min,time_max,type)
            cursor.execute(sql)
            row = cursor.fetchall()
            total = 0
            doortime_sumdict = {}
            for obj in row:
                total += obj[1]
            for obj in row:
                doortime_sumdict[obj[0]] = obj[1]/total
        return Response(data=doortime_sumdict)


# 告警管理效率
class WorkEfficiencyView(views.APIView):
    schema = AlarmNumStaticSchema
    def get(self, request):
        time_min = self.request.query_params.get('time_min', '')
        time_max = self.request.query_params.get('time_max', '')
        time_min = datetime.strptime(time_min, "%Y-%m-%d %H:%M:%S")
        time_max = datetime.strptime(time_max, "%Y-%m-%d %H:%M:%S")
        with connection.cursor() as cursor:
            sql = """select am_addtime, am_deal_time, sum(timestampdiff(minute, am_addtime, am_deal_time)) as dealtime
                        from scene_alarmmanagement
                        where am_addtime>='{}' and am_addtime<='{}'""".format(time_min,time_max)
            cursor.execute(sql)
            row = cursor.fetchall()
            print(row)

            # total = 0
            # doortime_sumdict = {}
            # for obj in row:
            #     total += obj[1]
            # for obj in row:
            #     doortime_sumdict[obj[0]] = obj[1]/total
        return Response(data=row)


# 场景管理
class SceneListView(generics.ListAPIView):
    queryset = Scene.objects.all()
    # queryset = Favor.objects.filter(user=request.user)error
    serializer_class = SceneSerializers


# 场景添加
class SceneAddView(generics.CreateAPIView):
    serializer_class = SceneAddSerializers
    # 自定义返回结果

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            # 失败信息的定制
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response(data={'code': 400, 'message': "添加失败", 'error': e}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # 成功后返回信息的定制

        res = Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        res.data['code'] = 200
        res.data['message'] = '添加成功'
        return res


# 场景更新
class SceneUpdateView(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Scene.objects.all()
    serializer_class = SceneAddSerializers

    def post(self, request, *args, **kwargs):
        try:
            self.update(request, *args, **kwargs)
        except Exception as e:
            return Response(data={'code': 400, 'message': '修改失败', 'error': e}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 200, 'message': '修改成功'}, status=status.HTTP_200_OK)


# 场景删除
class SceneDeleteView(views.APIView):

    # 重写destroy方法自定义返回结果
    def get(self, request, pk):
        # 获取地址url中的参数
        try:
            # 自定义试图手动调用check_object_permissions(get_object())验证对象
            obj = Scene.objects.get(pk=pk)
            self.check_object_permissions(request, obj)

            Scene.objects.get(pk=pk).delete()
        except Exception as e:
            return Response(data={'code': 400, 'message': '删除失败', 'error': e}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'code': 200, 'message': '删除成功'}, status=status.HTTP_200_OK)


# 场景浏览
class SceneBrowseView(views.APIView):
    def get(self,request):
        result = {}
        try:
            with connection.cursor() as cursor:
                sql = """select scene_name, scene_status, scene_addtime
                            from scene_scene"""
                cursor.execute(sql)
                scene = cursor.fetchall()
                result['scene'] = scene
            co2 = Co2.objects.last()
            pm25 = Pm25.objects.last()
            temperature = Temperature.objects.last()
            methane = Methane.objects.last()
            invade = Invade.objects.last()
            co2 = [co2.id, co2.co2_name, co2.co2_status, co2.co2_insert_time]
            pm25 = [pm25.id, pm25.pm25_name, pm25.pm25_status, pm25.pm25_insert_time]
            temperature = [temperature.id, temperature.temperature_name,temperature.temperature_status, temperature.temperature_insert_time]
            methane = [methane.id, methane.methane_name, methane.methane_status, methane.methane_insert_time]
            invade = [invade.id, invade.invade_name, ]
            result['equipments'] = [co2, pm25, temperature, methane, invade]
        except Exception as e:
            print(e)
            return Response(data={'code': 400, 'message': '删除失败', 'error': e}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'scene': scene, 'equipments': result['equipments']})


class EquipmentStatusView(views.APIView):
    def get(self, request):
        try:
            # 实时消防检测
            smoke = Smoke.objects.last()
            flame = Flame.objects.last()
            methane = Methane.objects.last()
            alarmlamp = Alarmlamp.objects.last()
            alertor = Alertor.objects.last()

            # 实时环境检测
            humidity = Humidity.objects.last()
            temperature = Temperature.objects.last()
            beam = Beam.objects.last()
            co2 = Co2.objects.last()
            pm25 = Pm25.objects.last()

            # 实时大屏
            display = Display.objects.last()
            # 实时设备检测
            light = Light.objects.last()
            fan = Fan.objects.last()
            pump = Pump.objects.last()
            unlocking1 = []
            # 实时安防检测
            print(len(Unlocking.objects.all().values()))
            if len(Unlocking.objects.all().values()) <= 4:
                unlocking1 = Unlocking.objects.all().values()[::-1]
                print(unlocking1)
            else:
                for i in range(1, 6):
                    unlocking1.append(Unlocking.objects.all()[-i])

            invade = Invade.objects.last()
            fire_control_check = [[smoke.smoke_name, smoke.smoke_status],
                                  [flame.flame_name, flame.flame_status],
                                  [methane.methane_name, methane.methane_status],
                                  [alarmlamp.alarmlamp_name, alarmlamp.alarmlamp_status],
                                  [alertor.alertor_name, alertor.alertor_status]]

            environment_check = [[humidity.humidity_name, humidity.humidity_online,humidity.humidity_value],
                                 [temperature.temperature_name, temperature.temperature_online, temperature.temperature_value],
                                 [beam.beam_name, beam.beam_online, beam.beam_value],
                                 [co2.co2_name, co2.co2_online, co2.co2_value],
                                 [pm25.pm25_name, pm25.pm25_online, pm25.pm25_value]]

            LCD = [display.display_name, display.display_content]
            equipment_check = [[light.light_name, light.light_status],
                               [fan.fan_name, fan.fan_status],
                               [pump.pump_name, pump.pump_status]]

            unlocking_log = unlocking1

            invade_check = [invade.invade_name,invade.invade_status]
        except Exception as e:
            return Response(data={'code': 400, 'message': '删除失败', 'error': e}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'消防检测': fire_control_check, '环境检测': environment_check, 'LCD屏幕': LCD,
                              '设备检查': equipment_check, '安防检查': unlocking_log, '入侵检测': invade_check})



