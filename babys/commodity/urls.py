# _*_coding:utf-8_*_
# 作者    : tanzikun
# 创建时间 : 2021/5/26 15:27
# 文件    : urls.py
# IDE    : PyCharm

from django.urls import path
from .views import *

urlpatterns = [
    path('.html', commodityView, name='commodity'),
    path('/detail.<int:id>.html', detailView, name='detail'),
    path('/collect.html', collectView, name='collect')
]