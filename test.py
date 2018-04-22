#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Hui
# @Date  : 2018/4/5
# @Desc  :

import investment
import sys
import pandas as pd

STOCK_LIST = '/home/chenhui/investment/data/my_stock/stock_china.xlsx'

if __name__ == '__main__':
    #sheet = pd.read_excel(STOCK_LIST, converters= {u'代码':str})
    #for index in sheet[u'代码']: save_data(index)
    #print('爬取完毕')

    #r=investment._get_stock_hist_eps('600900','2018-04-28')
    #r = investment.get_hist_data('600900')
    stockId = sys.argv[1]
    #df = investment.analyze_stock_ttm(stockId,ktype='W', start='2008-01-01')
    #print(df)
    #df = investment.load_pe_ttm_from_excel(stockId, start='2008-01-01',end=None)
    #investment.draw_pe_ttm(stockId, df)
    #爬取市场指数数据
    #investment.get_market_index_from_jiucaishuo('sh000905')
    #生成指数数据的图片
    #investment.draw_market_index_pe('hihsi', start='2009-01-01', end='2018-04-10')
    #investment.draw_market_index_pb('hihsi', start='2009-01-01', end='2018-04-10')
    #股票市盈率图片
    #investment.draw_stock_pe_ttm(stockId, start='2010-01-01')
    #股票市净率图片
    #investment.draw_stock_pb(stockId)
    #股票市盈率市净率图片
    #investment.draw_stock_pe_pb(stockId, start='2010-01-01')
    #股票财务指标分析
    #df = investment.load_stock_financial(stockId)
    #print(df)
    #财务成长能力表
    #grow = investment.GrowthTable(stockId, start=2009)
    #pic = grow.analyze_by_year()
    #print(pic)

    #财务盈利能力表
    profit = investment.ProfitabilityTable(stockId, start=2008)
    pic = profit.analyze_by_quater()
    print(pic)
    #营运能力报表
    #manage = investment.ManagementTable(stockId)
    #pic = manage.analyze_by_year()
    #print(pic)
