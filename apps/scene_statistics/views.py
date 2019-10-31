from django.shortcuts import render
from django.db import connection
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, views, mixins
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.
class FireView(views.APIView):
        def get(self,requst):
            try:
                with connection.cursor() as cursor:
                    sql = """
                    select am_content,sum(timestampdiff(minute , am_addtime, am_deal_time)) as sumtime
                    from scene_alarmmanagement
                    where am_type_id=2;
                    """
                cursor.execute(sql)
                row = cursor.fetchall()
                content = {}
                content['消防传感器'] = row
            except:
                return Response(data={'code': 400, 'message': '修改失败'}, status=status.HTTP_400_BAD_REQUEST, )
            return Response(data={'消防传感器': content}, status=status.HTTP_200_OK)
