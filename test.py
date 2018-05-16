#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Hui
# @Date  : 2018/4/5
# @Desc  :

import investment
import sys
import investment.util.cons as ct
import pandas as pd

STOCK_LIST = '/home/chenhui/investment/data/my_stock/all_china_stock.xlsx'

def analyze_stock(stockId):
    ct._save_data(stockId, investment.get_stock_fianacial_data_all_year(stockId, pd.DataFrame))
    print(investment.get_accountant_table_data(stockId, 'zcfzb'))
    print(investment.get_accountant_table_data(stockId, 'lrb'))
    print(investment.get_accountant_table_data(stockId, 'xjllb'))
    #财务成长能力
    grow = investment.GrowthTable(stockId, start=2008)
    print(grow.compare_by_year())
    print(grow.analyze_by_year())
    #财务盈利能力 bug
    profit = investment.ProfitabilityTable(stockId, start=2008)
    print(profit.analyze_by_quater())
    print(profit.analyze_profit_rate_by_year())
    # 营运能力报 bug
    manage = investment.ManagementTable(stockId)
    print(manage.analyze_by_year())
    #资产负债表
    balance = investment.BalanceSheet(stockId)
    print(balance.analyze_currency_by_year())
    print(balance.quick_analyze())
    # 现就流量表
    cash = investment.CashFlowStatement(stockId)
    print(cash.analyze_cashflow_by_year())
    # 利润表
    #profit = investment.ProfitStatement(stockId)
    #print(profit..)
    print(u'%s分析完毕'%stockId)

def choose_latest_years():
    sheet = pd.read_excel(STOCK_LIST, converters={'code': str})
    for index in sheet['code']:
        investment.choose_stock_from_china(index, start=2015)


def find_stock():
    sheet = pd.read_excel(STOCK_LIST, converters={'code': str})
    for index in sheet['code']:
        result = investment.find_quick_grow_stock(index)
        if result:
            print(u'成长股:%s' % index)
    print(u'简单寻找完毕')

if __name__ == '__main__':
    #sheet = pd.read_excel(STOCK_LIST, converters= {u'代码':str})
    #for index in sheet[u'代码']: save_data(index)
    #print('爬取完毕')

    #r=investment._get_stock_hist_eps('600900','2018-04-28')
    #r = investment.get_hist_data('600900')
    #stockId = sys.argv[1]
    #type = sys.argv[2]
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
    #analyze_stock(stockId)

    #选股
    #choose_latest_years()
    #for index in ['601318', '600900', '000001']:
    #    investment.choose_stock_from_china(index)
    find_stock()
    #利润表测试
    #lrb = investment.ProfitStatement(stockId)
    #lrb.quick_analyze()







