# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'app.views.index'),
    url(r'^about/', 'app.views.about'),
    url(r'^task/', 'app.views.task'),
    url(r'^testcase/', 'app.views.test_case'),
    url(r'^device/', 'app.views.device_module'),

)