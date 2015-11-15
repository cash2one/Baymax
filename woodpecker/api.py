# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

from rest_framework import viewsets
import serializer
from .models import Task, TestCase, User, Module


class DeviceModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = serializer.DeviceSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer