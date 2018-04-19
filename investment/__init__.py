#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Hui
# @Date  : 2018/4/3
# @Desc  :


__version__ = '0.0.1'
__author__ = 'Baby Chan'

"""
数据爬取模块
"""
from investment.crawl.financial_data import (get_stock_fianacial_data_all_year, get_hist_data)
from investment.crawl.trade import (get_china_stock_today, get_hongkong_stock_today,
                                    get_china_index_fund, get_china_etfn_fund,
                                    get_market_index, get_market_index_from_jiucaishuo)

"""
数据分析模块
"""
from investment.analyzation.financial import (_get_stock_hist_eps, analyze_stock_ttm,
                                              load_pe_ttm_from_excel, get_today_stock_ttm,
                                              suggest_stock_ttm, _get_stock_hist_pb,
                                              analyze_stock_pb)

"""
数据可视化模块
"""
from investment.analyzation.visualization import (draw_stock_pe_ttm, draw_market_index_pe,
                                                  draw_market_index_pb)

"""
数据持久化模块
"""
from investment.persistence.stock import (save_stock_pe_ttm, save_today_china_stock,
                                          save_today_hongkong_stock, save_stock_pb,
                                          save_market_index_his)
from investment.persistence.fund import (save_china_index_fund, save_china_etf_fund)

