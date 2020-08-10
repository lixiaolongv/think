#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 7:08 下午
# @Author  : BruceLee
# @Site    : 
# @File    : fisher.py

from app import create_app

app = create_app()

if __name__ == '__main__':
    # 生产环境服务器是：nginx + uwsgi
    app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=81)
