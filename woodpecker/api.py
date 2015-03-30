# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

from rest_framework import viewsets
import serializer
from .models import Task, TestCase, AppUser, DeviceModule


class DeviceModuleViewSet(viewsets.ModelViewSet):
    queryset = DeviceModule.objects.all()
    serializer_class = serializer.DeviceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = serializer.UserSerializer