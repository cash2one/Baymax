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


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label=u"用户名",
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"用户名",
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
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()