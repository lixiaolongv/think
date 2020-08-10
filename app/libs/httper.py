#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 7:41 上午
# @Author  : BruceLee
# @Site    : 
# @File    : httper.py

import requests


class HTTP:

    @staticmethod
    def get(url, return_json=True):
        """
        :param url:
        :param return_json: 判断返回的对象是否是json
        :return:
        """
        r = requests.get(url)
        if r.status_code != 200:
            return {"error": "GET Fail"} if return_json else "get request error"
        return r.json() if return_json else r.text

    @staticmethod
    def post(url, return_json=True, data=None, json=None, **kwargs):
        """
        :param url:
        :param return_json: 判断返回的对象是否是json
        :return:
        """
        r = requests.post(url, data, json, **kwargs)
        if r.status_code != 200:
            return {"error": "POST Fali"} if return_json else "post request error"
        return r.json() if return_json else r.text
