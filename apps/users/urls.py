from django.urls import path
from .views import *

app_name = '[users]'
urlpatterns = [
    path(r'userlist/<int:pk>/', UserListView.as_view(), name='userlist'),
    path(r'useradd/',UserAddView.as_view(),name='useradd'),
    path(r'userdele/<int:pk>/',UserDeleteView.as_view(),name='userdel'),
    path(r'userupd/<int:pk>/',UserUpdView.as_view(),name='userupd')
]