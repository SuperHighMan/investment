#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : stock.py
# @Author: Hui
# @Date  : 2018/4/9
# @Desc  :

import investment
import investment.util.cons as ct

def save_stock_pe_ttm(stockList, ktype='W', start='2008-01-01', end=None):
    """
    持久化存储股票的滚动市盈率
    :param stockList: list
                      股票列表 e.g. ['600900', '000002']
    :param ktype:     string, 默认为'W'
                      D=日线，W=周线，M=月线
    :param start:     string, 默认为'2008-01-01'
                      市盈率开始的时间
    :param end:       end, 默认为None
                      市盈率结束时间
    :return:          None
                      保存数据到磁盘
    """
    for stockId in stockList:
        try:
            df = investment.analyze_stock_ttm(stockId, ktype, start, end)
            df.to_excel(ct.LOCAL_DATA_PE_TTM%stockId)
            print(u'计算股票%s滚动市盈率完毕...数据已经保存'%stockId)
        except Exception as e:
            print(u'股票%s滚动市盈率计算出错'%stockId)

def save_stock_pb(stockList, ktype='W', start='2008-01-01', end=None):
    """
    持久化存储股票的历史市净率
    :param stockList: list
                      股票列表 e.g. ['600900', '000002']
    :param ktype:     string, 默认为'W'
                      D=日线，W=周线，M=月线
    :param start:     string, 默认为'2008-01-01'
                      市净率开始的时间
    :param end:       end, 默认为None
                      市净率结束时间
    :return:          None
                      保存数据到磁盘
    """
    for stockId in stockList:
        try:
            df = investment.analyze_stock_pb(stockId, ktype, start, end)
            df.to_excel(ct.LOCAL_DATA_PB%stockId)
            print(u'计算股票%s历史市净率完毕...数据已经保存' % stockId)
        except Exception as e:
            print(u'股票%s市净率计算出错' % stockId)

def save_today_china_stock():
    """
    持久化A股当天的数据
    :return:
    """
    date,df = investment.get_china_stock_today(step=80, pause=0.1)
    df.to_excel(ct.LOCAL_DATA_TODAY_MARKET%(ct.AREA_CODE['CHINA'],ct.INVEST_CODE['STOCK'], date))
    print(u'当天A股市场数据获取完毕...数据已保存')

def save_today_hongkong_stock():
    """
    持久化香港市场当天数据
    :return:
    """
    date,df = investment.get_hongkong_stock_today(step=80, pause=0.1)
    df.to_excel(ct.LOCAL_DATA_TODAY_MARKET%(ct.AREA_CODE['HONGKONG'], ct.INVEST_CODE['STOCK'], date))
    print(u'当天港股市场数据获取完毕...数据已保存')