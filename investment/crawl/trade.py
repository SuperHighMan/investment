#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : trade.py
# @Author: Hui
# @Date  : 2018/4/11
# @Desc  :
import investment.util.cons as ct
import investment.util.storage as st
import math
import requests
import time
import json
import pandas as pd
import lxml.html
from lxml import etree

def get_china_stock_today(step=80, pause=0.02):
    """
    获取今日A股市场所有的股票交易数据

    :param step:int
                默认80条记录
    :param pause:float 默认0.02秒
    :return:string, DataFrame
                日期，属性
    """
    nums = math.ceil(ct.MARKET_COUNT['china_stock']/step)
    df = pd.DataFrame()
    date = ''
    try:
        for page in range(nums):
            time.sleep(pause)
            url = ct.STOCK_CHINA_LATEST_URL%(ct.P_TYPE['http'], ct.DOMAINS['fianace_sina'], page+1, step)
            response = requests.get(url)
            response.encoding = 'utf-8'
            #code = json.loads(response.text)[0]['code']
            date = json.loads(response.text)[0]['day']
            #fields = json.loads(response.text)[0]['fields']
            items = json.loads(response.text)[0]['items']
            new_df = pd.DataFrame(items, columns=ct.DAY_TRADE_CHINA_COLUMNS)
            df = df.append(new_df, ignore_index=True)
        df = df.drop(['guba','favor'], axis=1)
        return date, df
    except Exception as e:
        print('获取全A市场数据出错')
        return None

def get_hongkong_stock_today(step=80, pause=0.02):
    """
    获取今日港股市场所有的股票交易数据
    :param step: int 默认一次获取80条
    :param pause: float 默认暂停0.02秒
    :return:string, DataFrame
             日期，属性
    """
    nums = math.ceil(ct.MARKET_COUNT['hongkong_stock']/step)
    df = pd.DataFrame()
    date = '%s-%s-%s'%(ct.NOW_YEAR, ct.NOW_MONTH, ct.NOW_DAY)
    try:
        for page in range(nums):
            time.sleep(pause)
            url = ct.STOCK_HONGKONG_LATEST_URL%(ct.P_TYPE['http'], ct.DOMAINS['fianace_sina'], page+1, step)
            response = requests.get(url)
            response.encoding = 'utf-8'
            items = json.loads(response.text)[0]['items']
            new_df = pd.DataFrame(items, columns=ct.DAY_TRADE_HONGKONG_COLUMNS)
            df = df.append(new_df, ignore_index=True)
        df = df.drop(['guba', 'favor'], axis=1)
        return date, df
    except Exception as e:
        print('获取港股市场出错')
        return None

def get_china_index_fund(type='zs', page =1, step=20, pause=0.02):
    """
    获取大陆境内的公募指数型基金
    :param page:int 默认第1页
    :param step:int 默认一次20
    :param pause:float 默认间隔0.02秒
    :return:string,DataFrame
    """
    r = int(time.time()) * 1000
    url = ct.INDEX_FUND_CHINA_URL%(ct.P_TYPE['http'], ct.DOMAINS['fund_eastmoney'], r, type, page)
    response = requests.get(url)
    response.encoding = 'utf-8'
    nums = math.ceil(json.loads(response.text)['TotalCount']/step)
    df = pd.DataFrame()
    date = '%s-%s-%s' % (ct.NOW_YEAR, ct.NOW_MONTH, ct.NOW_DAY)
    try:
        for page in range(nums):
            time.sleep(pause)
            url = ct.INDEX_FUND_CHINA_URL % (ct.P_TYPE['http'],
                                             ct.DOMAINS['fund_eastmoney'], r, type, page+1)
            response = requests.get(url)
            response.encoding = 'urf-8'
            new_df = pd.DataFrame(json.loads(response.text)['Datas'])
            df = df.append(new_df, ignore_index=True)
        return date, df
    except Exception as e:
        print('获取境内指数型基金出错')
        return None

def get_china_etfn_fund(type='etf'):
    """
    获取场内ETF交易基金
    :param type:
    :return:
    """
    url = ct.ETF_FUND_CHINA_URL%(ct.P_TYPE['http'], ct.DOMAINS['fund_eastmoney'])
    response = requests.get(url)
    response.encoding = 'gbk'
    doc =response.text.replace(u'行情', '')
    doc = doc.replace(u'基金吧', '')
    doc = lxml.html.document_fromstring(doc)
    tables = doc.xpath("//table[@id='oTable']")
    sarr = [etree.tostring(node).decode('utf-8') for node in tables]
    sarr = ''.join(sarr)
    sarr = '<table>%s</table>' % sarr
    dataArr = pd.read_html(sarr)[0]
    dataArr.drop(dataArr.index[[0,1]], inplace=True)
    dataArr.drop([0,1,2], axis=1, inplace=True)
    dataArr.columns = ct.DAY_EFT_FUND_COLUMNS
    dataArr = dataArr.set_index(u'基金代码')
    date = '%s-%s-%s' % (ct.NOW_YEAR, ct.NOW_MONTH, ct.NOW_DAY)
    return date, dataArr

def get_market_index(code, type='china', pause=0.02):
    """
    获取市场指数数据，如沪深300，中证500
    :param type: string 默认'china'
    :param pause: float 默认0.02秒
    :return: string,csv
             日期，文件
    """
    symbol = '0%s'%code if code[0] in ['0'] else '1%s'%code
    url = ct.MARKET_INDEX_URL%(ct.P_TYPE['http'], ct.DOMAINS['money_163'], symbol, '20010104','20180413')
    #print(url)
    response = requests.get(url)
    with open(st.LOCAL_DATA_MARKET_INDEX%('china',code), 'wb') as csv:
        csv.write(response.content)
    df = pd.read_csv(url, encoding='gbk')
    df = df.sort_values(by=u'日期', ascending=True)
    df = df.set_index(u'日期')
    df.to_csv(st.LOCAL_DATA_MARKET_INDEX%('china',code))
    return