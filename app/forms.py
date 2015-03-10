# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django import forms

class TaskForm(forms.Form):
    TaskName = forms.CharField(max_length=200)
    TaskType = forms.CharField(label='0')
    TaskCount = forms.CharField()
    TaskState = forms.CharField()
    DeviceType = forms.CharField(max_length=50)
    Description = forms.CharField(widget=forms.Textarea)
    CreateTime = forms.DateTimeField()
    UpdateTime = forms.DateTimeField()
    CreateWay = forms.CharField(max_length=50)
    IsShared = forms.BooleanField(required=False)