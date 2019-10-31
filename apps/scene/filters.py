from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import AlarmManagement


#告警过滤器
class AlarmFilter(rest_framework.FilterSet):
    time_min = rest_framework.DateTimeFilter(field_name='am_addtime',lookup_expr='gte')
    time_max = rest_framework.DateTimeFilter(field_name='am_addtime',lookup_expr='lte')

    class Meta:
        model = AlarmManagement
        fields = ['time_min','time_max','scene_id','am_type_id','am_level_id','am_status']

# class AlarmAdtimeFilter(rest_framework.FilterSet):
#     time_min = rest_framework.DateTimeFilter(field_name='am_addtime', lookup_expr='gte')
#     time_max = rest_framework.DateTimeFilter(field_name='am_addtime', lookup_expr='lte')
#
#     class Meta:
#         model = AlarmManagement
#         fields = ['time_min', 'time_max']
