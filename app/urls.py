# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'app.views.index'),
                       url(r'^about/', 'app.views.about'),

)