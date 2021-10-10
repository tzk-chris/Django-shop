#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： chrixtan
# datetime： 2021/8/19 15:59 
# ide： PyCharm

# index 的 urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # path('', indexView, name='index')
    path('', indexClassView.as_view(), name='index')
]