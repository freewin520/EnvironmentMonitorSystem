from django.urls import path
from .views import *

app_name = '[scene_statistics]'
urlpatterns = [
    # 警告管理
    path(r'fire_statistics/', FireView.as_view(), name='fire_statistics')
]