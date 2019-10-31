#from django.conf.urls import url
from django.conf.urls import url
from django.contrib import admin
import rest_framework.authtoken.views
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='环控原型 API')
# 14!

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api_token_auth/', obtain_jwt_token),
    url(r'^api/', schema_view),
    path(r'users/', include('users.urls', namespace='users')),# users
    path(r'scenes/',include('scene.urls', namespace='scenes')),
    path(r'scenes_statistics/',include('scene_statistics.urls', namespace='scenes_statistics')),
    path(r'operations/', include('operations.urls', namespace='operations')),
    # path(r'scene/',include('users.urls',namespace='users')),#scene
]
