#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : visualization.py
# @Author: Hui
# @Date  : 2018/4/9
# @Desc  :


import matplotlib.pyplot as plt

def draw_pe_ttm(stockId, dataArr):
    """
    绘制滚动市盈率曲线
    :param dataArr: DataFrame
                属性:date, pe_ttm, close
    :return: None
            曲线图
    """
    dataArr.plot()
    plt.title('%s TTM'%stockId)
    plt.grid()
    plt.show()
