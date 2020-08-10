#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 3:46 下午
# @Author  : BruceLee
# @Site    : 
# @File    : search_struct.py


class searchStruct:
    # 数据来源平台
    # SOURCE_TYPE_TAOBAO 淘宝；SOURCE_TYPE_PINDUODUO 拼多多； SOURCE_TYPE_JINGDONG 京东
    SOURCETYPE = "SOURCE_TYPE_TAOBAO"
    QUERY = "衣服"
    CURSOR = "0"
    SIZE = "2"
    SORT = "SORT_TYPE_INTEGRATED"
    ACTIONTYPE = "ACTION_TYPE_USER_CLICK"

    searchReq = {
        "sourceType": SOURCETYPE,
        "query": QUERY,
        "cursor": CURSOR,
        "size": SIZE,
        "sort": SORT,
        "filters": {
            "showLooting": False
        },
        "actionType": ACTIONTYPE
    }

    searchRes = {
        # 数据来源平台
        "platform": "taobao",
        # 商品ID
        "sourceIID": "1234",
        # 商品短标题
        "shortTitle": "衣服",
        # 商品图片
        "imageURL": "",
        # 购买者身份标志
        # "buyerIdentity": {
        #     # 用户ID
        #     "userId": "123",
        #     # 第一重身份
        #     "identityOne": "memerbership"
        # },
        # 自购奖励
        "buyNormalCash": "10",
        "buyNormalAllowance": "10",
        "membershipCash": "20",
        "membershipAllowance": "20",
        # 分享赚奖励
        "shareNormalCash": "5",
        "shareMembershipCash": "50"
    }
