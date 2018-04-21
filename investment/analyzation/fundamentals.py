#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : fundamentals.py
# @Author: Hui
# @Date  : 2018/4/21
# @Desc  :


import investment
import investment.util.cons as ct
import investment.util.storage as st
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

class GrowthTable:
    """
    成长能力报表
    """
    def __init__(self, stockId, start=2008, end=2018):
        """
        :param stockId:string 股票代码 e.g. 600900
        :param start:int
        :param end:int
        """
        self.stockId = stockId
        self.start = start
        self.end = end
        self.df = investment.load_stock_financial(stockId, '%d-01-01'%start, '%d-12-31'%end)

    def analyze_by_year(self):
        """
        按照年度分析股票的成长能力：
        34主营业务收入增长率、
        35净利润增长率、
        36净资产增长率、
        37总资产增长率
        :return:string 图片路径
        """
        by_year = [(ct.Q4%year) for year in range(self.start, self.end+1)]
        df = self.df[[34,35,36,37]]
        df = df[df.index.isin(by_year)]
        df.index = df.index.map(lambda x: x[:4])
        df[34] = df[34].astype('float64')
        df[35] = df[35].astype('float64')
        df[36] = df[36].astype('float64')
        df[37] = df[37].astype('float64')
        #划分成四个子图
        plt.figure(22, facecolor='lightgrey')
        plt.suptitle('%s成长能力分析'%self.stockId, fontsize=20, color='gray', alpha=0.4)
        # 子图1.主营业务收入增长率
        plt.subplot(221)
        plt.bar(df.index, df[34],width=0.4, alpha=0.8)
        plt.title(u'主营业务收入增长率（%）')
        for a, b in zip(df.index, df[34]): plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom')
        # 子图2.
        plt.subplot(222)
        plt.bar(df.index, df[35],width=0.4, alpha=0.8)
        plt.title(u'净利润增长率（%）')
        for a, b in zip(df.index, df[35]): plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom')
        # 子图3.
        plt.subplot(223)
        plt.bar(df.index, df[36],width=0.4, alpha=0.8)
        plt.title(u'净资产增长率（%）')
        for a, b in zip(df.index, df[36]): plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom')
        # 子图4.
        plt.subplot(224)
        plt.bar(df.index, df[37],width=0.4, alpha=0.8)
        plt.title(u'总资产增长率（%）')
        for a,b in zip(df.index, df[37]): plt.text(a, b+0.05, '%.2f'%b, ha='center', va='bottom')
        plt.tight_layout(pad=0.3, w_pad=0.4, h_pad=1.0)
        plt.text(0.75, 0.45, ct.AUTHOR, rotation=15,
                 fontsize=30, color='lightcoral',
                 ha='center', va='center', alpha=0.4)
        plt.savefig(st.PIC_STOCK % (self.stockId, ct.FINANCIAL_TABLE['growth']), dpi=200)
        return st.PIC_STOCK % (self.stockId, ct.FINANCIAL_TABLE['growth'])
        #plt.show()