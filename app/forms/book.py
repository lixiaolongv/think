#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 11:28 上午
# @Author  : BruceLee
# @Site    : 验证层的验证对象
# @File    : book.py

from wtforms import Form, StringField, IntegerField
from wtforms.validators import length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), length(min=1, max=30)])  # message=""默认提示信息
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
