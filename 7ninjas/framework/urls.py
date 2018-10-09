from django.conf.urls import url, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatters = [
    url(r'^', include(router.urls)),
    url(r'^framework-auth/', include('rest_framework.urls', namespace='rest_framework'))
]