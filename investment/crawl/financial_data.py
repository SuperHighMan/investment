#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : financial_data.py
# @Author: Hui
# @Date  : 2018/4/3
# @Desc  :

import requests
import lxml.html
from lxml import etree
import pandas as pd
import time
import json
from investment.util import cons as ct


def _get_stock_fianacial_data(stockId, year, dataArr, retry_count=3, pause=2):
    """
    获取某支股票某一年的财务指标
    :param stockId: string
                   股票代码 e.g. 600900
    :param year:    int
                   财务指标年份
    :param dataArr: DataFrame

    :param retry_count:int, 默认为3
    :param pause:   float, 默认为2
    :return: DataFrame
                   属性: 指标数据,2017-12-31,2017-09-30,2017-06-30,2017-01-31
    """
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            response = requests.get(ct.FINICIAL_URL % (ct.P_TYPE['http'], ct.DOMAINS['fianace_sina'],
                                    stockId, year))
            response.encoding = 'gbk'
            doc = lxml.html.document_fromstring(response.text)
            tables = doc.xpath("//table[@id='BalanceSheetNewTable0']/tbody/tr")
            sarr = [etree.tostring(node).decode('utf-8') for node in tables]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>' % sarr
            dataArr = pd.read_html(sarr)[0]
            return dataArr
        except Exception as e:
            #print(u'获取财务指标出错')
            pass

def get_stock_fianacial_data_all_year(stockId, dataArr):
    """
    获取某支股票历史上所有的财务指标数据
    :param stockId: string
                    股票代码 e.g. 600900
    :param dataArr: DataFrame
    :return:        DataFrame
                    属性:指标数据,2017-12-31,...2016-12-31,...2015-12-31,...
    """
    dataArr = _get_stock_fianacial_data(stockId, ct.NOW_YEAR-1, pd.DataFrame())
    year = ct.NOW_YEAR-1
    for _ in range(30):
        year = year - 1
        tmp = _get_stock_fianacial_data(stockId, year, pd.DataFrame())
        if tmp is not None:
            dataArr = pd.merge(dataArr, tmp, on=0)
        else:
            print(u'注意:抓取的股票%s财务指标从%d年开始往前没有历史数据'%(stockId, year))
            break
    return dataArr


def get_hist_data(code=None, ktype='W',start=None, end=None, retry_count=3, pause=2):
    """
    获取某只股票的历史记录
    :param code:string
                股票代码 e.g. 600900
    :param ktype:string
                D=日线 W=周 M=月，默认为D
    :param retry_count: int, 默认为3
    :param pause: int, 默认为2
    :return:DataFrame
                属性:日期，开盘价，最高价，收盘价，最低价，成交量，价格变动，涨跌幅，5日均价，
                    10日均价，20日均价，5日均量，10日均量，20日均量，换手率
    """
    url = ct.DAY_PRICE_URL%(ct.P_TYPE['http'], ct.DOMAINS['ifeng'],
                            ct.K_TYPE[ktype], ct._code_to_symbol(code))
    for _ in range(retry_count):
        time.sleep(pause)
        try:
            response = requests.get(url)
            js = json.loads(response.text)
            if len(js['record'][0]) == 15:
                cols = ct.DAY_PRICE_COLUMNS
                df = pd.DataFrame(js['record'], columns=cols)
                if start is not None:
                    df = df[df.date >= start]
                if end is not None:
                    df = df[df.date <= end]
                #for col in cols[1:]:
                #    df[col] = df[col].astype(float)
                df = df.set_index('date')

                return df
            else:
                return None
        except Exception as e:
            print('获取股票数据失败')
            pass

