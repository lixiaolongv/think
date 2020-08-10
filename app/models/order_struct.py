#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 5:18 下午
# @Author  : BruceLee
# @Site    : 
# @File    : order_struct.py
"""
"user_id": user_id,  # 购买者
            "share_user_id": share_user_id,  # 分享者
            "source_type": platform,  # 平台,1淘宝,3京东
            "item_ids": product_id,  # 商品ID
            "tk_status": 12,  # # 订单状态,3订单结算,12订单付款,13订单失效,14订单成功
            "type": order_type,  # 订单类型,0普通订单,1拉新订单,2预售定金订单,默认0
            "env": 2,
            "commission_rate": 10000,  # 10000
            "next": {
                "tk_status": tk_status,
                "interval": 20
            }
"""


class OrderStruct:
    # 用户ID，取值正整数，默认值0
    USERID = 1111
    # 分享者ID，取值正整数，默认值0
    SHAREUSERID = 0
    # 平台, 取值正整数，默认值1淘宝,3京东
    PLATFORM = 1
    # 商品ID, 默认空列表[]
    ITEMIDS = "123456"
    # 当前订单状态,3订单结算,12订单付款,13订单失效,14订单成功
    CURRENTTKSTATUS = 12
    # 订单类型,0普通订单,1拉新订单,2预售定金订单,默认0
    TYPE = 1
    # 环境
    ENV = 2
    # 兑换兑率，默认10000
    COMMISSIONRATE = 10000
    # 下一订单状态,3订单结算,12订单付款,13订单失效,14订单成功
    NEXTTKSTATUS = 14
    # 间隔时间, 默认60s
    INTERVAL = 60
    # 支付价格
    PRICE = 5000

    orderReq = {
        "user_id": USERID,
        "share_user_id": SHAREUSERID,
        "source_type": PLATFORM,
        "item_ids": ITEMIDS,
        "tk_status": CURRENTTKSTATUS,
        "type": TYPE,
        "env": ENV,
        "commission_rate": COMMISSIONRATE,
        "next": {
            "tk_status": NEXTTKSTATUS,
            "interval": INTERVAL
        }
    }

    takeoutReq = {
        "user_id": USERID,
        "source_type": PLATFORM,  # 4饿了么，5美团，7KFC
        "tk_status": CURRENTTKSTATUS,
        "pay_price": PRICE,
        "commission_rate": COMMISSIONRATE,
        "type": TYPE,  # 订单类型,0普通订单,1拉新订单,2预售定金订单,3维权订单 默认0
        "next": {
            "tk_status": NEXTTKSTATUS,  # 订单状态,3订单结算,12订单付款,13订单失效,14订单成功
            "interval": INTERVAL
        }
    }