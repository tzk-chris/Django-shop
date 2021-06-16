# _*_coding:utf-8_*_
# 作者    : tanzikun
# 创建时间 : 2021/5/26 15:27
# 文件    : urls.py
# IDE    : PyCharm

from django.urls import path
from .views import *

urlpatterns = [
    path('.html', shopperView, name='shopper'),
    path('/login.html', loginView, name='login'),
    path('/logout.html', logoutView, name='logout'),
    path('/shopcart.html', shopcartView, name='shopcart'),
]