#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : storage.py
# @Author: Hui
# @Date  : 2018/4/17
# @Desc  :

import os

HOME_DIR = '/home/chenhui'
BASE_DIR = 'investment/data'
PIC_DIR = 'investment/pic'
#股票财务指标数据
LOCAL_DATA_FINANCIAL = os.path.join(HOME_DIR, BASE_DIR,'my_stock/%s.xlsx')
#股票会计表数据
LOCAL_DATA_ACCOUNTANT = os.path.join(HOME_DIR, BASE_DIR, 'table/%s/%s-%s.csv')
#股票历史交易数据
LOCAL_DATA_DAY_PRICE = os.path.join(HOME_DIR,BASE_DIR,'my_stock_day_price/%s.xlsx')
#股票pe、pb数据
LOCAL_DATA_PE_TTM = os.path.join(HOME_DIR,BASE_DIR,'stock_pe_ttm/%s-pe_ttm.xlsx')
LOCAL_DATA_PB = os.path.join(HOME_DIR,BASE_DIR,'stock_pb/%s-pb.xlsx')
#今日市场数据
LOCAL_DATA_TODAY_MARKET = os.path.join(HOME_DIR,BASE_DIR,'today/%s-%s-%s.xlsx')
#指数基金存储路径
LOCAL_DATA_INDEX_FUND = os.path.join(HOME_DIR,BASE_DIR,'fund/index/%s-%s-%s-%s.xlsx')
LOCAL_DATA_ETF_FUND = os.path.join(HOME_DIR,BASE_DIR,'fund/etf/%s-%s-%s-%s.xlsx')
LOCAL_DATA_MARKET_INDEX = os.path.join(HOME_DIR,BASE_DIR,'market-index/%s-%s.csv')
#指数pe、pb存储路径
LOCAL_DATA_JIUCAI_INDEX = os.path.join(HOME_DIR,BASE_DIR,'jiucai/all.xlsx')
LOCAL_DATA_JIUCAI_PE = os.path.join(HOME_DIR,BASE_DIR,'jiucai/pe/%s-%s.xlsx')
LOCAL_DATA_JIUCAI_PB = os.path.join(HOME_DIR,BASE_DIR,'jiucai/pb/%s-%s.xlsx')
#主流指数数据图片路径
PIC_INDEX_PE = os.path.join(HOME_DIR, PIC_DIR, 'index/%s-%s.jpg')
PIC_INDEX_PB = os.path.join(HOME_DIR, PIC_DIR, 'index/%s-%s.jpg')
#股票数据图片路径
PIC_STOCK = os.path.join(HOME_DIR, PIC_DIR, 'stock/%s-%s.jpg')