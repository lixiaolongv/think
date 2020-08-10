#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 11:55 下午
# @Author  : BruceLee
# @Site    : 
# @File    : order_source.py

"""
url = "http://betaapi.shmiao.net:10909/sapi/v2/order/simulate"
        requestBody = {
            "user_id": user_id,  # 购买者
            "source_type": platform,  # 平台,1淘宝,3京东，2拼多多
            # "share_user_id": shareUserId,  # 分享者，把这个share_user_id隐藏，则属于自购
            "item_ids": product_id,  # 商品ID
            "tk_status": 12,  # # 订单状态,3订单结算,12订单付款,13订单失效,14订单成功
            "type": order_type,  # 订单类型,0普通订单,1拉新订单,2预售定金订单,3维权订单 默认0
            "env": 5,
            # "pay_price": 1111,  # 支付金额，以分为单位
            "commission_rate": 10000,  # 10000
            "next": {
                "tk_status": tk_status,
                "interval": 20
            }
        }
        token = "Bearer 9527-{0}".format(user_id)
        requestBody1 = json.dumps(requestBody)
        headers = {
            "Authorization": token,
            'Content-Type': 'application/json; charset=utf-8'
        }
        resp = requests.post(url, requestBody1, headers=headers, verify=False)
        return resp
"""
import copy
from ..models.order_struct import OrderStruct
from flask import json
from app.libs.httper import HTTP
from flask import current_app


class Order:
    order_simulate_url = "http://betaapi.shmiao.net:10909/sapi/v2/order/simulate"

    @classmethod
    def order_ok(cls, user_id, product_id, platform):
        """
        palce order ok
        :param user_id:
        :param product_id:
        :return:
        """
        requestBody = cls.finishing_order_req(user_id, product_id, platform)
        headers = cls.get_headers(user_id)
        resp = HTTP.post(cls.order_simulate_url, data=requestBody, headers=headers, verify=False)
        return resp

    @classmethod
    def order_takeout_ok(cls, user_id, platform):
        """
        palce takeout order ok
        :param user_id:
        :return:
        """
        print(type(platform))
        print(platform)
        requestBody = cls.finish_takeout_req(user_id, platform)
        print(requestBody)
        headers = cls.get_headers(user_id)
        print(headers)
        resp = HTTP.post(cls.order_simulate_url, data=requestBody, headers=headers, verify=False)
        print(cls.order_simulate_url)
        print(resp)
        return resp

    @classmethod
    def order_presale(cls, user_id, product_id, platform):
        """
        palce order taobao presale
        :param user_id:
        :param product_id:
        :param order_type: presale=2
        :return:
        """
        requestBody = cls.finishing_order_req(user_id, product_id, platform, order_type=2)
        headers = cls.get_headers(user_id)
        resp = HTTP.post(cls.order_simulate_url, data=requestBody, headers=headers, verify=False)
        return resp

    @classmethod
    def order_cancel(cls, user_id, product_id, platform):
        """
        palce order cancel
        :param user_id:
        :param product_id:
        :return:
        """
        requestBody = cls.finishing_order_req(user_id, product_id, platform, next_tk_status=13)
        headers = cls.get_headers(user_id)
        resp = HTTP.post(cls.order_simulate_url, data=requestBody, headers=headers, verify=False)
        return resp

    @classmethod
    def order_takeout_cancel(cls, user_id, platform):
        """
        palce takeout order cancel
        :param user_id:
        :return:
        """
        requestBody = cls.finish_takeout_req(user_id, platform, next_tk_status=13)
        print(requestBody)
        headers = cls.get_headers(user_id)
        print(headers)
        resp = HTTP.post(cls.order_simulate_url, data=requestBody, headers=headers, verify=False)
        return resp

    @classmethod
    def order_right(cls, user_id, product_id, platform):
        """
        palce order right
        :param user_id:
        :param product_id:
        :return:
        """
        requestBody = cls.finishing_order_req(user_id, product_id, platform, order_type=3)
        headers = cls.get_headers(user_id)
        resp = HTTP.post(cls.order_simulate_url, data=requestBody, headers=headers, verify=False)
        return resp

    @classmethod
    def order_takeout_right(cls, user_id, platform):
        """
        palce takeout order right
        :param user_id:
        :param product_id:
        :return:
        """
        requestBody = cls.finish_takeout_req(user_id, platform, order_type=3)
        headers = cls.get_headers(user_id)
        resp = HTTP.post(cls.order_simulate_url, data=requestBody, headers=headers, verify=False)
        return resp

    @staticmethod
    def finishing_order_req(user_id, product_id, platform, share_user_id=0, order_type=1, next_tk_status=14,
                            next_status_time=20, is_coupon=True):
        """
        finishing order request
        :param user_id:
        :param product_id:
        :param share_user_id:
        :param order_type:
        :param next_tk_status:
        :param next_status_time:
        :param is_coupon:
        :return:
        """
        order_struct_copy = copy.deepcopy(OrderStruct.orderReq)

        if user_id:
            order_struct_copy["user_id"] = int(user_id)

        if product_id:
            order_struct_copy["item_ids"] = str(product_id)

        if share_user_id:
            order_struct_copy["share_user_id"] = int(share_user_id)
        else:
            del order_struct_copy["share_user_id"]

        if int(platform) == current_app.config["SOURCE_TYPE_TAOBAO"]:
            order_struct_copy["source_type"] = current_app.config["SOURCE_TYPE_TAOBAO"]
        elif int(platform) == current_app.config["SOURCE_TYPE_PDD"]:
            order_struct_copy["source_type"] = current_app.config["SOURCE_TYPE_PDD"]
        elif int(platform) == current_app.config["SOURCE_TYPE_JD"]:
            order_struct_copy["source_type"] = current_app.config["SOURCE_TYPE_JD"]

        if order_type != 1:
            order_struct_copy["type"] = order_type

        if next_tk_status != 14:
            order_struct_copy["next"]["tk_status"] = next_tk_status

        if next_status_time != 20:
            order_struct_copy["interval"] = next_status_time

        req = json.dumps(order_struct_copy)
        return req

    @classmethod
    def finish_takeout_req(cls, user_id, platform=4, order_type=1, next_tk_status=14, next_status_time=20, attr=True):
        """
        elme & meituan & KFC finish orderReq
        :param user_id:
        :param platform:
        :param order_type:
        :param next_tk_status:
        :param next_status_time:
        :param attr:
        :return:
        """
        order_struct_copy = copy.deepcopy(OrderStruct.takeoutReq)
        if user_id:
            order_struct_copy["user_id"] = int(user_id)

        print(int(platform) != 1)
        if int(platform) != 1:
            order_struct_copy["source_type"] = int(platform)

        if order_type != 1:
            order_struct_copy["type"] = order_type

        if next_tk_status != 14:
            order_struct_copy["next"]["tk_status"] = next_tk_status

        if next_status_time != 20:
            order_struct_copy["interval"] = next_status_time

        req = json.dumps(order_struct_copy)
        return req

    @staticmethod
    def get_token(user_id):
        """
        get token by userid
        :return:
        """
        return "Bearer 9527-{0}".format(user_id)

    @classmethod
    def get_headers(cls, user_id):
        """
        get headers by userid
        :return:
        """
        headers = {
            "Authorization": cls.get_token(user_id),
            "Content-Type": 'application/json; charset=utf-8'
        }
        return headers
