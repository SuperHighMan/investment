#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cons.py
# @Author: Hui
# @Date  : 2018/4/3
# @Desc  :

import datetime
import investment
import pandas as pd

NOW_YEAR = datetime.datetime.now().year
NOW_MONTH = datetime.datetime.now().month
NOW_DAY = datetime.datetime.now().day

LOCAL_DATA_FINANCIAL = '/home/chenhui/investment/data/my_stock/%s.xlsx'
LOCAL_DATA_DAY_PRICE = '/home/chenhui/investment/data/my_stock_day_price/%s.xlsx'
LOCAL_DATA_PE_TTM = '/home/chenhui/investment/data/stock_pe_ttm/%s-pe_ttm.xlsx'
LOCAL_DATA_PB = '/home/chenhui/investment/data/stock_pb/%s-pb.xlsx'
LOCAL_DATA_TODAY_MARKET = '/home/chenhui/investment/data/today/%s-%s-%s.xlsx'

LOCAL_DATA_INDEX_FUND = '/home/chenhui/investment/data/fund/index/%s-%s-%s-%s.xlsx'
LOCAL_DATA_ETF_FUND = '/home/chenhui/investment/data/fund/etf/%s-%s-%s-%s.xlsx'
LOCAL_DATA_MARKET_INDEX = '/home/chenhui/investment/data/market-index/%s-%s.csv'

K_TYPE = {'D': 'akdaily', 'W': 'akweekly', 'M':'akmonthly'}
P_TYPE = {'http': 'http://', 'ftp': 'ftp://'}
DOMAINS = {'fianace_sina': 'money.finance.sina.com.cn', 'ifeng': 'ifeng.com',
           'fund_eastmoney': 'fund.eastmoney.com', 'money_163': 'quotes.money.163.com'}
INVEST_CODE = {'STOCK': 'stock', 'FUND': 'fund'}
AREA_CODE = {'CHINA':'china', 'HONGKONG':'hongkong'}
FINICIAL_VIRABLES = {'date': 0, 'eps': 4, 'bv': 7}
MARKET_COUNT = {'china_stock': 3447, 'hongkong_stock': 2103}

DAY_PRICE_COLUMNS = ['date', 'open', 'high', 'close', 'low', 'volume', 'price_change', 'p_change',
                     'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20', 'turnover']
DAY_TRADE_CHINA_COLUMNS = ['symbol', 'code', 'name', 'trade', 'pricechange', 'changepercent', 'buy', 'sell',
                     'settlement', 'open', 'high', 'low', 'volume', 'amount', 'ticktime', 'per', 'per_d',
                     'nta', 'pb', 'mktcap', 'nmc', 'turnoverratio', 'favor', 'guba']
DAY_TRADE_HONGKONG_COLUMNS = ["symbol","name","engname","tradetype","lasttrade","prevclose","open",
                              "high","low","volume","currentvolume","amount","ticktime","buy","sell",
                              "high_52week","low_52week","eps","dividend","stocks_sum","pricechange",
                              "changepercent","favor","guba"]
DAY_EFT_FUND_COLUMNS = ['基金代码', '基金简称', '单位净值', '累计净值', '昨日单位净值', '昨日累计净值',
                       '增长值', '增长率', '市价', '折价率']

FINICIAL_URL = '%s%s/corp/go.php/vFD_FinancialGuideLine/stockid/%s/ctrl/%s/displaytype/4.phtml'
DAY_PRICE_URL = '%sapi.finance.%s/%s/?code=%s&type=last'
STOCK_CHINA_LATEST_URL = '%s%s/d/api/openapi_proxy.php/?__s=[[\"hq\",\"hs_a\",\"\",0,%d,%d]]'
STOCK_HONGKONG_LATEST_URL = '%s%s/d/api/openapi_proxy.php/?__s=[[\"hk\",\"qbgg_hk\",\"\",0,%d,%d]]'
INDEX_FUND_CHINA_URL = '%s%s/data/FundChannelData_BaseInfoHandler.ashx?r=%d&m=%s&pageIndex=%d&sName=isbuy&s=desc&t=all'
ETF_FUND_CHINA_URL ='%s%s/ETFN_jzzzl.html'
MARKET_INDEX_URL = '%s%s/service/chddata.html?code=%s&start=%s&end=%s&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER'

def _code_to_symbol(code):
    """
    编码转换工具
    :param code:string
                股票代码 e.g. 600900
    :return:string
                代号 e.g. sh600900
    """
    if len(code) !=6 :
        return code
    else:
        return 'sh%s'%code if code[0] in ['5', '6', '9'] else 'sz%s'%code


def _save_data(stockId, df):
    """
    保存数据
    :param stockId:string e.g. 600900
    :param df:DataFrame
    :return:None
    """
    #df = investment.get_stock_fianacial_data_all_year(stockId, pd.DataFrame())
    df.to_excel(LOCAL_DATA_FINANCIAL%stockId)
    print('股票%s财务指标爬取完毕'%stockId)