#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : financial.py
# @Author: Hui
# @Date  : 2018/4/8
# @Desc  :

import os
import pandas as pd
import investment.util.cons as ct
import investment

def analyze_stock_ttm(stockId, ktype='W',start='2008-01-01',end=None):
    """
    分析某支股票的滚动市盈率
    :param stockId:string
                  股票代码 e.g. 600900
    :param ktype,默认为'W'
    :param start,默认为'2008-01-01'
    :param end,默认为None
    :return:DataFrame
                属性：日期，pe_ttm，收市价格
    """
    data_path = ct.LOCAL_DATA_DAY_PRICE%stockId
    df = None
    if os.path.exists(data_path):
        df = pd.read_excel(data_path)
    else:
        df = investment.get_hist_data(stockId, ktype, start)
    ttm = [float(df.loc[date,'close'])/_get_stock_hist_eps(stockId, date) for date in df.index.tolist()]
    ttm = pd.Series(ttm, name='pe_ttm', index=df.index.tolist())
    df.insert(1,'pe_ttm', ttm)
    df = df[['pe_ttm', 'close']]
    return df

def get_today_stock_ttm(stockId, date, per=30):
    """
    计算某支股票当前的滚动市盈率
    :param stockId: string
                    股票代码 e.g. 600900
    :param date:    string
                    日期
    :param per:     int
                    百分位
    :return:dict
                    回测数据
    """
    dict = {}
    df = pd.read_excel(ct.LOCAL_DATA_TODAY_MARKET%('china', 'stock', date),
                       converters={u'code':str, u'trade':float})
    df = df.set_index('code')
    eps = _get_stock_hist_eps(stockId, date)
    price = df.loc[stockId]['trade']
    pe_ttm = price/eps
    dict['pe_ttm'] = float('%.2f'%pe_ttm)
    dict['code'] = stockId
    dict['eps'] = eps
    dict['price'] = float('%.2f'%price)
    df = load_pe_ttm_from_excel(stockId)
    count = 0
    sum = 0
    for his in df[u'pe_ttm']:
        sum = sum +1
        if pe_ttm > his:
            count = count + 1
    dict['percentage'] = float('%.4f'%(count/sum)) * 100
    dict['suggest_price'] = float('%.2f'%(eps*suggest_stock_ttm(stockId, percentage=per)))
    return dict

def suggest_stock_ttm(stockId, percentage=30):
    """
    分析适合的股价，按照pe估值百分位
    :param stockId:string 股票代码
    :param percentage:int 百分位
    :return:float
            市盈率
    """
    df = load_pe_ttm_from_excel(stockId)
    list = sorted(df[u'pe_ttm'])
    index = int(len(list)*percentage/100) - 1
    return list[index]

def _get_stock_hist_eps(stockId, date):
    """
    计算股票历史时间的每股收益eps
    :param stockId:string
                   股票代码 e.g. 600900
    :param date:string
                   历史时间 e.g. 2015-10-31
    :return:float
                   返回TTM
    """
    data_path = ct.LOCAL_DATA_FINANCIAL%stockId
    df = None
    eps = None
    # read data from local
    if os.path.exists(data_path):
        df = pd.read_excel(data_path)
    # read data from network
    else:
        df = investment.get_stock_fianacial_data_all_year(stockId, pd.DataFrame())
        ct._save_data(stockId, df)
    #date_list = df.loc[0].values[0:-1]
    date_list = [i for i in df.loc[ct.FINICIAL_VIRABLES['date']]]

    year,month,day = date.split('-')
    try:
        if (date >= '%s-01-01' % year) & (date <= '%s-03-31' % year):
            col = date_list.index('%s-12-31' % str(int(year)-1))
            eps = float(df.iloc[ct.FINICIAL_VIRABLES['eps'], col])
            eps = float('%.4f' % eps)
            #print('第一季度')
        elif (date >= '%s-04-01' % year) & (date <= '%s-06-30' % year):
            col1 = date_list.index('%s-12-31' % str(int(year) - 1))
            col2 = date_list.index('%s-03-31' % year)
            col3 = date_list.index('%s-03-31' % str(int(year) - 1))
            eps = float(df.iloc[ct.FINICIAL_VIRABLES['eps'], col1]) - \
                  float(df.iloc[ct.FINICIAL_VIRABLES['eps'], col3]) + \
                  float(df.iloc[ct.FINICIAL_VIRABLES['eps'], col2])
            eps = float('%.4f' % eps)
            #print('第二季度')
        elif (date >= '%s-07-01' % year) & (date <= '%s-09-30' % year):
            col1 = date_list.index('%s-12-31' % str(int(year) - 1))
            col2 = date_list.index('%s-06-30' % year)
            col3 = date_list.index('%s-06-30' % str(int(year) - 1))
            eps = float(df.iloc[ct.FINICIAL_VIRABLES['eps'], col1]) - \
                  float(df.iloc[ct.FINICIAL_VIRABLES['eps'], col3]) + \
                  float(df.iloc[ct.FINICIAL_VIRABLES['eps'], col2])
            #eps = float('%.4f' % eps)
            #print('第三季度')
        elif (date >= '%s-10-01' % year) & (date <= '%s-12-31' % year):
            col1 = date_list.index('%s-12-31' % str(int(year) - 1))
            col2 = date_list.index('%s-09-30' % year)
            col3 = date_list.index('%s-09-30' % str(int(year) - 1))
            eps = float(df.iloc[ct.FINICIAL_VIRABLES['eps'], col1]) - \
                  float(df.iloc[ct.FINICIAL_VIRABLES['eps'], col3]) + \
                  float(df.iloc[ct.FINICIAL_VIRABLES['eps'], col2])
            #eps = float('%.4f' % eps)
            #print('第四季度')
        else:
            print('日期格式错误')
        return eps
    except Exception as e:
        if int(month) <= 3:
            year = str(int(year) - 1).zfill(4)
            month = '12'
            day = '31'
        else:
            month = str(int(month) - 3).zfill(2)
        #print('最新季报未更新')
        return _get_stock_hist_eps(stockId, '%s-%s-%s'%(year, month, day))

def _get_stock_hist_pb(stockId, date):
    """
    计算股票历史市净率
    :param stockId:string
                   股票代码 e.g. 600900
    :param date:string
                   历史时间 e.g. 2015-01-01
    :return:float
            每股净资产
    """
    data_path = ct.LOCAL_DATA_FINANCIAL % stockId
    df = None
    # read data from local
    if os.path.exists(data_path):
        df = pd.read_excel(data_path)
    # read data from network
    else:
        df = investment.get_stock_fianacial_data_all_year(stockId, pd.DataFrame())
        ct._save_data(stockId, df)
    #date_list = df.loc[0].values[0:-1]
    date_list = [i for i in df.loc[ct.FINICIAL_VIRABLES['date']]]

    year,month,day = date.split('-')
    try:
        col = None
        if (date >= '%s-01-01' % year) & (date <= '%s-03-31' % year):
            col = date_list.index('%s-12-31' % str(int(year)-1))
        elif (date >= '%s-04-01' % year) & (date <= '%s-06-30' % year):
            col = date_list.index('%s-03-31' % year)
        elif (date >= '%s-07-01' % year) & (date <= '%s-09-30' % year):
            col = date_list.index('%s-06-30' % year)
        elif (date >= '%s-10-01' % year) & (date <= '%s-12-31' % year):
            col = date_list.index('%s-09-30' % year)
        bv = float(df.iloc[ct.FINICIAL_VIRABLES['bv'], col])
        bv = float('%.4f' % bv)
        return bv
    except Exception as e:
        if int(month) <= 3:
            year = str(int(year) - 1).zfill(4)
            month = '12'
            day = '31'
        else:
            month = str(int(month) - 3).zfill(2)
        #print('最新季报未更新')
        return _get_stock_hist_pb(stockId, '%s-%s-%s'%(year, month, day))

def analyze_stock_pb(stockId, ktype='W',start='2008-01-01',end=None):
    """
    分析某支股票的历史市净率
    :param stockId:string
                   股票代码 e.g. 600900
    :param ktype:string, 默认为'w'
    :param start:string, 默认为'2008-01-01'
    :param end:string,默认None
    :return:DataFrame
            属性，pb_ttm，收市价格
    """
    data_path = ct.LOCAL_DATA_DAY_PRICE % stockId
    df = None
    if os.path.exists(data_path):
        df = pd.read_excel(data_path)
    else:
        df = investment.get_hist_data(stockId, ktype, start)
    pb = [float(df.loc[date,'close'])/_get_stock_hist_pb(stockId, date) for date in df.index.tolist()]
    pb = pd.Series(pb, name='pb', index=df.index.tolist())
    df.insert(1,'pb', pb)
    df = df[['pb', 'close']]
    return df


def load_pe_ttm_from_excel(stockId, start='2008-01-01', end=None):
    """
    从表格中加载滚动市盈率
    :param stockId:string
                   股票代码 e.g. 600900
    :param start:  string 默认为'2008-01-01'
    :param end:    string 默认为None
    :return:       DataFrame
                   属性:date, pe_ttm, close
    """
    data_path = ct.LOCAL_DATA_PE_TTM%stockId
    if os.path.exists(data_path):
        df = pd.read_excel(data_path, converters={'pe_ttm':float,'close':float})
        if start is not None:
            df = df[df.date >= start]
        if end is not None:
            df = df[df.date <= end]
        #df = df.set_index('date')
        return df
    else:
        return None