# coding=utf-8
__author__ = 'guguohai@outlook.com'

from django import forms


class TaskForm(forms.Form):
    TaskName = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    TaskType = forms.CharField(label='0', widget=forms.TextInput(attrs={'class': 'form-control'}))
    TaskCount = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    TaskState = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    DeviceType = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','rows':'3'}))
    CreateTime = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    UpdateTime = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    CreateWay = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    IsShared = forms.BooleanField(required=False)


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名",
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"用户名",
                'class': 'input-large col-xs-12'
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label=u"密码",
        error_messages={'required': u'请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': u"密码",
                'class': 'input-large col-xs-12'
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()