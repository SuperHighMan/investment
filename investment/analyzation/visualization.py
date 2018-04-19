#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : visualization.py
# @Author: Hui
# @Date  : 2018/4/9
# @Desc  :

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import  MultipleLocator
import investment
import investment.util.storage as st
import investment.util.cons as ct

def draw_stock_pe_ttm(stockId, start='1990-01-01', end=None):
    """
    绘制滚动市盈率曲线
    :param stockId:string e.g. 600900
    :param start:默认'1900-01-01'
    :param end:默认None
    :return:
    """
    df = investment.load_pe_ttm_from_excel(stockId, start, end)
    #if df != None:
    df['date'] = pd.to_datetime(df['date'])
    #df = df.set_index('date')
    #市盈率 左边的y轴
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(df.date, df.pe_ttm)
    ax1.yaxis.set_major_locator(MultipleLocator(5.0))
    ax1.yaxis.set_minor_locator(MultipleLocator(1.0))
    ax1.yaxis.grid(True, which='major', color='red', linestyle='solid')
    ax1.yaxis.grid(True, which='minor', color='gray', linestyle='dashed')
    ax1.legend(['ttm'], loc='upper left')
    #股价 右边的y轴
    ax2 = ax1.twinx()
    ax2.plot(df.date, df.close, 'r', color='g')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
    ax2.xaxis.set_major_locator(mdates.YearLocator())
    ax2.xaxis.set_minor_locator(mdates.MonthLocator())
    ax2.xaxis.grid(True, which='minor', color='gray', linestyle='dashed')
    ax2.legend(['close'], loc='upper right')
    plt.title('%s TTM'%stockId)
    plt.show()
    #else:
        #print(u'对不起,没有股票%s的历史数据'%stockId)

def draw_market_index_pe(code, start='1990-01-01', end='2018-04-19'):
    """
    绘制指数滚动适应图
    :param code:strng e.g. sh000905
    :param start:string 默认'1900-01-01'
    :param end:string 默认'2018-04-19'
    :return:
    """
    path_pe = st.LOCAL_DATA_JIUCAI_PE%(code, ct.JIUCAI_CONS[0])
    if os.path.exists(path_pe):
        df = pd.read_excel(path_pe)
        df= df[df['gu_date'] >= start]
        df= df[df['gu_date'] <= end]
        df['gu_date'] = pd.to_datetime(df['gu_date'])
        df.plot(x='gu_date', y=ct.JIUCAI_CONS[0])

        ax = plt.gca()
        # 设置主刻度标签位置,标签文本的格式
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.yaxis.set_major_locator(MultipleLocator(5.0))
        # 显示次刻度标签的位置,没有标签文本
        ax.xaxis.set_minor_locator(mdates.MonthLocator())
        ax.yaxis.set_minor_locator(MultipleLocator(1.0))
        # 设置网格
        ax.xaxis.grid(True, which='minor', color='gray', linestyle='dashed')
        ax.yaxis.grid(True, which='major', color='red', linestyle='solid')
        ax.yaxis.grid(True, which='minor', color='gray', linestyle='dashed')
        #设置x标签
        ax.set_xlabel('')
        plt.title(u'%s TTM'%code)
        plt.savefig(st.PIC_INDEX_PE%(code, ct.JIUCAI_CONS[0]), dpi=200)
        #plt.show()
    else:
        print(u'对不起,没有指数:%s的滚动市盈率数据'%code)

def draw_market_index_pb(code, start='1990-01-01', end='2018-04-19'):
    """
    绘制指数滚动市净率图
    :param code:strng e.g. sh000905
    :param start:string 默认'1900-01-01'
    :param end:string 默认'2018-04-19'
    :return:
    """
    path_pb = st.LOCAL_DATA_JIUCAI_PE % (code, ct.JIUCAI_CONS[1])
    if os.path.exists(path_pb):
        df = pd.read_excel(path_pb)
        df = df[df['gu_date'] >= start]
        df = df[df['gu_date'] <= end]
        df['gu_date'] = pd.to_datetime(df['gu_date'])
        df.plot(x='gu_date', y=ct.JIUCAI_CONS[1])

        ax = plt.gca()
        # 设置主刻度标签位置,标签文本的格式
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.yaxis.set_major_locator(MultipleLocator(0.5))
        # 显示次刻度标签的位置,没有标签文本
        ax.xaxis.set_minor_locator(mdates.MonthLocator())
        ax.yaxis.set_minor_locator(MultipleLocator(0.1))
        # 设置网格
        ax.xaxis.grid(True, which='minor', color='gray', linestyle='dashed')
        ax.yaxis.grid(True, which='major', color='yellow', linestyle='solid')
        ax.yaxis.grid(True, which='minor', color='gray', linestyle='dashed')
        ax.set_xlabel('')
        plt.title(u'%s TTM'%code)
        plt.savefig(st.PIC_INDEX_PB%(code, ct.JIUCAI_CONS[1]), dpi=200)
        #plt.show()
    else:
        print(u'对不起,没有指数:%s的滚动市净率数据'%code)