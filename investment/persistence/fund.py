#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : fund.py
# @Author: Hui
# @Date  : 2018/4/12
# @Desc  :


import investment
import investment.util.cons as ct
import investment.util.storage as st

def save_china_index_fund():
    """
    持久化境内指数型基金
    :return:
    """
    date, df = investment.get_china_index_fund(type='zs', page=1, step=20, pause=0.1)
    df.to_excel(st.LOCAL_DATA_INDEX_FUND%(ct.AREA_CODE['CHINA'], ct.INVEST_CODE['FUND'],'zs', date))
    print(u'截至%s号，境内指数型(普通开放型)基金抓取完毕...数据已保存'%(date))

    date, df = investment.get_china_index_fund(type='qdii', page=1, step=20, pause=0.1)
    df.to_excel(st.LOCAL_DATA_INDEX_FUND%(ct.AREA_CODE['CHINA'], ct.INVEST_CODE['FUND'], 'qdii', date))
    print(u'截至%s号，境内指数型(QDII)基金抓取完毕...数据已保存' % (date))

def save_china_etf_fund():
    """
    持久化境内etf基金
    :return:
    """
    date, df = investment.get_china_etfn_fund(type='etf')
    df.to_excel(st.LOCAL_DATA_ETF_FUND%(ct.AREA_CODE['CHINA'], ct.INVEST_CODE['FUND'], 'etf', date))
    print(u'截至%s号，场内ETF基金抓取完毕...数据已保存' % (date))