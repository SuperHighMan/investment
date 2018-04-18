#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : storage.py
# @Author: Hui
# @Date  : 2018/4/17
# @Desc  :

import os

HOME_DIR = '/home/chenhui'
BASE_DIR = 'investment/data'

LOCAL_DATA_FINANCIAL = os.path.join(HOME_DIR, BASE_DIR,'my_stock/%s.xlsx')
LOCAL_DATA_DAY_PRICE = os.path.join(HOME_DIR,BASE_DIR,'my_stock_day_price/%s.xlsx')
LOCAL_DATA_PE_TTM = os.path.join(HOME_DIR,BASE_DIR,'stock_pe_ttm/%s-pe_ttm.xlsx')
LOCAL_DATA_PB = os.path.join(HOME_DIR,BASE_DIR,'stock_pb/%s-pb.xlsx')
LOCAL_DATA_TODAY_MARKET = os.path.join(HOME_DIR,BASE_DIR,'today/%s-%s-%s.xlsx')

LOCAL_DATA_INDEX_FUND = os.path.join(HOME_DIR,BASE_DIR,'fund/index/%s-%s-%s-%s.xlsx')
LOCAL_DATA_ETF_FUND = os.path.join(HOME_DIR,BASE_DIR,'fund/etf/%s-%s-%s-%s.xlsx')
LOCAL_DATA_MARKET_INDEX = os.path.join(HOME_DIR,BASE_DIR,'market-index/%s-%s.csv')

LOCAL_DATA_JIUCAI_INDEX = os.path.join(HOME_DIR,BASE_DIR,'jiucai/all.xlsx')
LOCAL_DATA_JIUCAI_PE = os.path.join(HOME_DIR,BASE_DIR,'jiucai/pe/%s-%s.xlsx')
LOCAL_DATA_JIUCAI_PB = os.path.join(HOME_DIR,BASE_DIR,'jiucai/pb/%s-%s.xlsx')