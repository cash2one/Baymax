# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

from rest_framework import serializers
from .models import Task, TestCase, AppUser, DeviceModule


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceModule
        fields = ('ModuleName', 'IsEnable', 'Description')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ('UserName', 'DisplayName', 'Email')