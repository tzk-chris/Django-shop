#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： chrixtan
# datetime： 2021/8/19 16:08 
# ide： PyCharm

from django.urls import path
from .views import *

urlpatterns = [
    path('.html', commodityView, name='commodity'),
    path('/detail.<int:id>.html', detailView, name='detail'),
    path('/collect.html', collectView, name='collect')
]