#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : all_pe_ttm.py
# @Author: Hui
# @Date  : 2018/4/9
# @Desc  :

import investment
import pandas as pd

STOCK_LIST = '/home/chenhui/investment/data/my_stock/stock_china.xlsx'

#市场指数列表，包括沪深300，中证500等
MARKET_INDEX_LIST = '/home/chenhui/investment/data/fund/StandarIndexCode.xlsx'



def get_all_pb():
    """
    计算所有股票的历史市净率
    :return:
    """
    sheet = pd.read_excel(STOCK_LIST, converters={u'代码':str})
    #investment.save_stock_pe_ttm(sheet[u'代码'], ktype='W', start='2008-01-01', end=None)

    investment.save_stock_pb(sheet[u'代码'], ktype='W', start='2008-01-01', end=None)

    print('我的股票池计算完毕')

def get_all_pe():
    """
    计算所有股票的滚动市盈率
    :return:
    """
    sheet = pd.read_excel(STOCK_LIST, converters={u'代码':str})
    investment.save_stock_pe_ttm(sheet[u'代码'], ktype='W', start='2008-01-01', end=None)
    print('我的股票池计算完毕')


def get_all_market_index():
    """
    获取市场上所有的指数数据
    :return:
    """
    sheet = pd.read_excel(MARKET_INDEX_LIST, converters={'StandarIndexCode':str})
    investment.save_market_index_his(sheet['StandarIndexCode'])

if __name__ == '__main__':
    get_all_market_index()
    print(u'指数数据获取完毕')