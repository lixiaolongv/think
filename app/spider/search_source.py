#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 4:32 下午
# @Author  : BruceLee
# @Site    : 
# @File    : search_source.py
import copy

from ..libs.helper import get_headers
from ..libs.httper import HTTP
from ..models.search_struct import searchStruct
from flask import current_app, json


class Search:
    search_url = "https://betaapi.shmiao.net/search.Default/SearchItemList"

    @classmethod
    def search_productId(cls, user_id, platform=1):
        """
        search product taobao & jingdong & pinduoduo productId
        :param user_id:
        :param platform:
        :return:
        """
        requestBody = cls.finish_search_req(platform)
        headers = get_headers(user_id)
        resp = HTTP.post(cls.search_url, data=requestBody, headers=headers, verify=False)
        result = cls.finish_search_res(resp)
        return result

    @classmethod
    def finish_search_req(cls, platform=1):
        """
        finish search request info
        :param platform:
        :return:
        """
        search_struct_copy = copy.deepcopy(searchStruct.searchReq)

        if int(platform) == current_app.config["SOURCE_TYPE_TAOBAO"]:
            search_struct_copy["sourceType"] = "SOURCE_TYPE_TAOBAO"
        elif int(platform) == current_app.config["SOURCE_TYPE_PINDUODUO"]:
            search_struct_copy["sourceType"] = "SOURCE_TYPE_PINDUODUO"
        elif int(platform) == current_app.config["SOURCE_TYPE_JINGDONG"]:
            search_struct_copy["sourceType"] = "SOURCE_TYPE_JINGDONG"

        req = json.dumps(search_struct_copy)
        print(req)
        return req

    @classmethod
    def finish_search_res(cls, resp):
        """
        return seaarch response by struct
        :param resp:
        :return:
        """
        response_list = []
        product_list = resp["list"]

        for item in range(len(product_list)):
            search_res_copy = copy.deepcopy(searchStruct.searchRes)

            search_res_copy["platform"] = product_list[item]["base"]["sourceType"]
            search_res_copy["sourceIID"] = product_list[item]["base"]["sourceIID"]
            search_res_copy["shortTitle"] = product_list[item]["base"]["shortTitle"]
            search_res_copy["imageURL"] = product_list[item]["base"]["imageURL"]

            search_res_copy["buyNormalCash"] = product_list[item]["activityInfo"]["bonusInfo"]["buyBonus"]["normal"][0]["assetAmount"]

            search_res_copy["buyNormalAllowance"] = product_list[item]["activityInfo"]["bonusInfo"]["buyBonus"]["normal"][1]["assetAmount"]

            search_res_copy["membershipCash"] = product_list[item]["activityInfo"]["bonusInfo"]["buyBonus"]["membership"][0]["assetAmount"]

            search_res_copy["membershipAllowance"] = product_list[item]["activityInfo"]["bonusInfo"]["buyBonus"]["membership"][1]["assetAmount"]

            search_res_copy["shareNormalCash"] = product_list[item]["activityInfo"]["bonusInfo"]["shareBonus"]["normal"][0]["assetAmount"]

            search_res_copy["shareMembershipCash"] = product_list[item]["activityInfo"]["bonusInfo"]["shareBonus"]["membership"][1]["assetAmount"]

            response_list.append(search_res_copy)

        return response_list

