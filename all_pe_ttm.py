#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : all_pe_ttm.py
# @Author: Hui
# @Date  : 2018/4/9
# @Desc  :

import investment
import pandas as pd

STOCK_LIST = '/home/chenhui/investment/data/my_stock/stock_china.xlsx'



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


if __name__ == '__main__':
    get_all_pe()