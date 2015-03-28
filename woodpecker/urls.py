# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'woodpecker.views.index'),
    url(r'^home/', 'woodpecker.views.index'),
    url(r'^about/', 'woodpecker.views.about'),
    url(r'^task/', 'woodpecker.views.task'),
    url(r'^testcase/$', 'woodpecker.views.test_case'),
    url(r'^device/$', 'woodpecker.views.device_module'),
    url(r'^login/', 'woodpecker.views.login'),
    url(r'^logout/', 'woodpecker.views.logout'),

)