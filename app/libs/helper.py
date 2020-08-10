#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 11:07 下午
# @Author  : BruceLee
# @Site    : 自己封装的小模块
# @File    : helper.py


def is_isbn_or_key(word):
    """
    判断是isbn还是关键字请求
    :param word: 关键字
    :return:
    """
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit:
        isbn_or_key = "isbn"
    short_word = word.replace("-", "")
    if "-" in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = word
    return isbn_or_key


def get_token(user_id):
    """
    get token by userid
    :return:
    """
    return "Bearer 9527-{0}".format(user_id)


def get_headers(user_id):
    """
    get headers by userid
    :return:
    """
    headers = {
        "Authorization": get_token(user_id),
        "Content-Type": 'application/json; charset=utf-8'
    }
    return headers
