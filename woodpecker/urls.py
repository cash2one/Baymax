# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django.conf.urls import patterns, include, url
from .models import DeviceModule

from rest_framework import routers
import api

router = routers.DefaultRouter()
router.register(r'device', api.DeviceModuleViewSet)
router.register(r'user', api.UserViewSet)

urlpatterns = patterns('',
    url(r'^$', 'woodpecker.views.index'),
    url(r'^home/', 'woodpecker.views.index'),
    url(r'^about/', 'woodpecker.views.about'),
    url(r'^task/', 'woodpecker.views.task'),
    url(r'^testcase/$', 'woodpecker.views.test_case'),
    url(r'^device/$', 'woodpecker.views.device_module'),
    url(r'^login/', 'woodpecker.views.login'),
    url(r'^logout/', 'woodpecker.views.logout'),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)