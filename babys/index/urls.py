# _*_coding:utf-8_*_
# 作者    : tanzikun
# 创建时间 : 2021/5/26 10:19
# 文件    : urls.py
# IDE    : PyCharm

from django.urls import path
from .views import *

urlpatterns = [
    # path('', indexView, name='index')
    path('', indexClassView.as_view(), name='index')
]
