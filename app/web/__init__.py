#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 8:38 上午
# @Author  : BruceLee
# @Site    : 管理整个web类页面的视图函数，整理数据输出给前端
# @File    : __init__.py.py
from flask import Blueprint

web = Blueprint("web", __name__)

# 导入视图函数，若放在注册蓝图之前则会报错，这样的结构会出现循环导入
from app.web import book
