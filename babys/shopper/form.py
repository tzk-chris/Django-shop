#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： chrixtan
# datetime： 2021/9/11 20:43 
# ide： PyCharm

from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=11, label='请您输入手机号',
                               widget=forms.widgets.TextInput(
                                   attrs={'class': 'layui-input', 'placeholder': '请您输入手机号',
                                          'lay-verify': 'required|phone', 'id': 'username'}),)
    password = forms.CharField(max_length=20, label='请您输入密码',
                               widget=forms.widgets.PasswordInput(
                                   attrs={'class': 'layui-input', 'placeholder': '请您输入密码',
                                          'lay-verify': 'required|password', 'id': 'password'}),)

    # 自定义表单字段username的数据清洗
    def clean_username(self):
        if len(self.cleaned_data['username']) == 11:
            return self.cleaned_data['username']
        else:
            raise ValidationError('用户名为手机号码')