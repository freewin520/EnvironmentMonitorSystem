# *_*coding:utf-8 *_*
from django.urls import path
from operations import views

app_name = '[operations]'
urlpatterns = [
    # 日志列表
    path(r'logslist/', views.LogsListView.as_view(), name='logslist'),
    # 视频列表
    path(r'videolist/',views.VideoListView.as_view(),name='videolist'),
    # 视频添加
    path(r'videoadd/',views.VideoAddView.as_view(),name='videoadd'),
    # 视频删除
    path(r'videodel/<str:pks>/',views.VideoDelView.as_view(),name='videodel'),
    # 视频更新
    path(r'videoupd/<int:pk>/',views.VideoUpdView.as_view(),name='videoupd'),
    # 门禁列表
    path(r'doorapprove/',views.DoorApproveView.as_view(),name='doorapprove'),
    # 门禁申请
    path(r'dooradd/',views.DoorApproveAddView.as_view(),name='dooradd'),
    # 门禁修改
    path(r'doorupdate/',views.DoorApproveUpdView.as_view(),name='doorupdate'),
    # 门禁开门次数
    path(r'doornumber/',views.DoorApproveNumView.as_view(),name='doornumber'),
    # 各用户开门总时间占比
    path(r'doortimesum/',views.DoortimesumView.as_view(),name='doortimesum'),


]
