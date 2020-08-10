#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 8:38 上午
# @Author  : BruceLee
# @Site    : APP的初始化工作
# @File    : __init__.py.py
from flask import Flask


def create_app():
    # 实例化flask对象
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app


def register_blueprint(app):
    """
    把蓝图注册到Flask的APP核心对象上
    :param app:
    :return:
    """
    from app.web.book import web
    app.register_blueprint(web)
