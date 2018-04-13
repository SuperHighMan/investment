#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Hui
# @Date  : 2018/4/5
# @Desc  :

import investment
import pandas as pd

STOCK_LIST = '/home/chenhui/investment/data/my_stock/stock_china.xlsx'

if __name__ == '__main__':
    #sheet = pd.read_excel(STOCK_LIST, converters= {u'代码':str})
    #for index in sheet[u'代码']: save_data(index)
    #print('爬取完毕')

    #r=investment._get_stock_hist_eps('600900','2018-04-28')
    #r = investment.get_hist_data('600900')
    stockId = '600036'
    #df = investment.analyze_stock_ttm(stockId,ktype='W', start='2008-01-01')
    #print(df)
    df = investment.load_pe_ttm_from_excel(stockId, start='2008-01-01',end=None)
    print(df)
    investment.draw_pe_ttm(stockId, df)