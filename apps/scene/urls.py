from django.urls import path
from .views import *

app_name = '[scene]'
urlpatterns = [
    # 警告管理
    path(r'alarm/', AlarmListView.as_view(), name='alarm'),
    # 警告批量处理
    path(r'alarm_batch_process/', AlarmBatchProcessView.as_view(), name='alarm_batch_process'),
    # 警告处理
    path(r'alarm_process/', AlarmProcessView.as_view(), name='alarm_process'),
    # 警告批量审核
    path(r'alarm_batch_check/', AlarmBatchCheckView.as_view(), name='alarm_batch_process'),
    # 警告审核
    path(r'alarm_check/', AlarmCheckView.as_view(), name='alarm_check'),
    # 警告查看
    path(r'alarm_view/<int:pk>/', AlarmView.as_view(), name='alarm_view'),
    # 警告统计
    path(r'alarm_num1statics/',AlarmNum1StaticView.as_view(), name='alarm_num1statics'),
    # 警告状态数量统计
    path(r'alarm_num2statics/<int:type>/', AlarmNum2StaticView.as_view(), name='alarm_num2statics'),
    # 警告处理效率
    path(r'work_efficiency/', WorkEfficiencyView.as_view(), name='work_efficiency'),
    # 场景管理
    path(r'scenelist/', SceneListView.as_view(), name='scenelist'),
    # 场景新增
    path(r'sceneadd/', SceneAddView.as_view(), name='sceneadd'),
    # 场景更新
    path(r'sceneupdate/<int:pk>/', SceneUpdateView.as_view(), name='sceneupdate'),
    # 场景删除
    path(r'scenedelete/<int:pk>/', SceneDeleteView.as_view(), name='scenedelete'),
    # 场景浏览
    path(r'scenebrowse/', SceneBrowseView.as_view(), name='scenebrowse'),
    # 设备状态浏览
    path(r'equipmentstatus/', EquipmentStatusView.as_view(), name='equipmentstatus')
]