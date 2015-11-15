# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

from rest_framework import serializers
from .models import Task, TestCase, User, Module


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Module
        fields = ('ModuleName', 'IsEnable', 'Description')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('UserName', 'DisplayName', 'Email')