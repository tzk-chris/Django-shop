#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： chrixtan
# datetime： 2021/8/19 16:09 
# ide： PyCharm

from django.urls import path
from .views import *

urlpatterns = [
    path('.html', shopperView, name='shopper'),
    path('/login.html', loginView, name='login'),
    path('/logout.html', logoutView, name='logout'),
    path('/shopcart.html', shopcartView, name='shopcart'),
    path('/delete.html', deleteAPI, name='delete')
]
