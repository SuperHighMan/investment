#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : prioritizing.py
# @Author: Hui
# @Date  : 2018/5/8
# @Desc  :

import investment
import investment.util.cons as ct

def choose_stock_from_china(stockId, start=2013, end=2018):
    """

    :param stockList:股票代码
    :return:list
            优胜列表
    """
    #print(investment.get_accountant_table_data(stockId, 'zcfzb'))
    #print(investment.get_accountant_table_data(stockId, 'lrb'))
    #print(investment.get_accountant_table_data(stockId, 'xjllb'))
    balance = investment.BalanceSheet(stockId, start, end)
    df = balance.quick_analyze()
    result = df[df[ct.PROFITSTATEMENT['E']]>1]
    if len(result.index) >= 3:
        print(stockId)

def find_quick_grow_stock(stockId, start='2017-01-01', end='2018-12-31'):
    """
    默认查找最近一年的成长股，通过毛利率、净利率、营业收入增长率、营业利润增长率来搜索
    :param stockId:
    :param start:
    :param end:
    :return:
    """
    result = True
    try:
        lrb = investment.ProfitStatement(stockId)
        df = lrb.quick_analyze()
        df = df[df.index >= start]
        df = df[df.index <= end]
        columns = [u'毛利率', u'净利率', u'营业收入增长率', u'营业利润增长率']
        # 要求毛利率 > 30
        for i in range(len(df[u'毛利率'])):
            if df[u'毛利率'][i] < 30.0:
                result = False
        # 要求净利率 > 12
        for i in range(len(df[u'净利率'])):
            if df[u'净利率'][i] < 12.0:
                result = False
        # 要求营业收入快速增长
        for i in range(len(df[u'营业收入增长率'])-1):
            if df[u'营业收入增长率'][i]*0.9 >= df[u'营业收入增长率'][i+1]:
                result = False
        # 要求营业利润快速增长
        for i in range(len(df[u'营业利润增长率'])-1):
            if df[u'营业利润增长率'][i]*0.9 >= df[u'营业利润增长率'][i+1]:
                result = False
    except Exception as e:
        print(u'数据出错%s' % stockId)
        result = False
        return result
    return result