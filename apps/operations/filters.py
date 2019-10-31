# *_*coding:utf-8 *_*
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Logs,DoorApprove


#日志过滤器
class LogsFilter(rest_framework.FilterSet):
    time_min = rest_framework.DateTimeFilter(field_name='log_addtime',lookup_expr='gte')
    time_max = rest_framework.DateTimeFilter(field_name='log_addtime',lookup_expr='lte')
    class Meta:
        model = Logs
        fields = ['time_min','time_max','scene', 'log_module']

#门禁用户次数过滤器
class DoorFilter(rest_framework.FilterSet):
    time_min = rest_framework.DateTimeFilter(field_name='door_addtime',lookup_expr='gte')
    time_max = rest_framework.DateTimeFilter(field_name='door_addtime',lookup_expr='lte')
    class Meta:
        model = DoorApprove
        fields = ['time_min','time_max']

#门禁过滤器
class DoorApproveFilter(rest_framework.FilterSet):
    addtime_min = rest_framework.DateTimeFilter(field_name='door_addtime', lookup_expr='gte')
    addtime_max = rest_framework.DateTimeFilter(field_name='door_addtime', lookup_expr='lte')
    approvetime_min = rest_framework.DateTimeFilter(field_name='approve_time',lookup_expr='gte')
    approvetime_max = rest_framework.DateTimeFilter(field_name='approve_time',lookup_expr='lte')
    class Meta:
        model = DoorApprove
        fields = ['addtime_min','addtime_max','approvetime_min', 'approvetime_max','door_status']