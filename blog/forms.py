# coding=utf-8
__author__ = 'guguohai@pathbook.com.cn'

from django import forms


class ArticleForm(forms.Form):
    Title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    Content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '8'}))
    Description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}))
    Tags = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
