#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : fundamentals.py
# @Author: Hui
# @Date  : 2018/4/21
# @Desc  :

import pandas as pd
import investment
import investment.util.cons as ct
import investment.util.storage as st
import matplotlib.pyplot as plt
from functools import reduce
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

    def __mark_pic(self,plt, text):
        """
        添加水印
        :param plt:pyplot
        :param text:string
        """
        plt.tight_layout(pad=0.3, w_pad=0.4, h_pad=1.0)
        plt.text(0.75, 0.45, text, rotation=15,
                 fontsize=30, color='lightcoral',
                 ha='center', va='center', alpha=0.4)
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
        columns = [34,35,36,37]
        titles ={34:u'主营业务收入增长率（%）',
                 35:u'净利润增长率（%）',
                 36:u'净资产增长率（%）',
                 37:u'总资产增长率（%）'}
        df = self.df[columns]
        df = df[df.index.isin(by_year)]
        df.index = df.index.map(lambda x: x[:4])
        for i in columns:
            df[i] = df[i].map(lambda x:0 if x=='--' else float(x))
        #划分成四个子图
        figure = plt.figure(22, facecolor='lightgrey')
        plt.suptitle(u'%s成长能力分析'%self.stockId, fontsize='xx-large', color='gray', alpha=0.4)
        for i in columns:
            ax = figure.add_subplot(2,2,columns.index(i)+1)
            ax.bar(df.index, df[i],width=0.4, alpha=0.8)
            plt.title(titles[i])
            for a, b in zip(df.index, df[i]):
                plt.text(a, b + 0.05, '%.2f' % b, ha='center', va='bottom', fontsize='xx-small')
        self.__mark_pic(plt, ct.AUTHOR)
        plt.savefig(st.PIC_STOCK % (self.stockId, ct.FINANCIAL_TABLE['growth']), dpi=200)
        return st.PIC_STOCK % (self.stockId, ct.FINANCIAL_TABLE['growth'])
        #plt.show()

    def compare_by_year(self):
        """
        按照年度分析股票的成长能力：
        重点关注：营业收入增长率与营业利润增长率的关系
        净资产增长率与总资产增长率的关系
        :return:
        """
        by_year = [(ct.Q4 % year) for year in range(self.start, self.end + 1)]
        columns = [34, 35, 36, 37]
        titles = {34: u'主营业务收入增长率（%）',
                  35: u'净利润增长率（%）',
                  36: u'净资产增长率（%）',
                  37: u'总资产增长率（%）'}
        df = self.df[columns]
        df = df[df.index.isin(by_year)]
        for i in columns:
            df[i] = df[i].map(lambda x:0 if x=='--' else float(x))
        figure, (ax1,ax2) = plt.subplots(2, 1)
        ax1.plot(df[[columns[0], columns[1]]], alpha=0.8)
        ax1.legend([titles[columns[0]], titles[columns[1]]])
        ax1.set_xticklabels(df.index.map(lambda x: x[0:4]))
        ax2.plot(df[[columns[2], columns[3]]], alpha=0.8)
        ax2.legend([titles[columns[2]], titles[columns[3]]])
        ax2.set_xticklabels(df.index.map(lambda x: x[0:4]))
        self.__mark_pic(plt, ct.AUTHOR)
        plt.savefig(st.PIC_STOCK % (self.stockId, ct.FINANCIAL_TABLE['growth-tang']), dpi=200)
        return st.PIC_STOCK % (self.stockId, ct.FINANCIAL_TABLE['growth-tang'])

class ProfitabilityTable:
    """
    盈利能力报表
    """
    def __init__(self, stockId, start=2008, end=2018):
        """
        :param stockId:
        :param start:
        :param end:
        """
        self.stockId = stockId
        self.start = start
        self.end = end
        self.df = investment.load_stock_financial(stockId, '%d-01-01'%start, '%d-12-31'%end)

    def __mark_pic(self,plt, text):
        plt.tight_layout(pad=0.3, w_pad=0.4, h_pad=1.0)
        plt.text(0.75, 0.45, text, rotation=15,
                 fontsize=30, color='lightcoral',
                 ha='center', va='center', alpha=0.4)

    def analyze_by_quater(self):
        """
        按照年度分析股票的盈利能力:
        17. 营业利润率（%）
        19. 销售净利润（%）
        29. 主营业务利润（元）
        32. 扣除非经常性损益后的净利润(元)
        :return: string 图片路径
        """
        #by_year = [(ct.Q4 % year) for year in range(self.start, self.end + 1)]
        columns = [17,19,29,32]
        titles= {17:u'营业利润率（%）',
                      19:u'销售净利润（%）',
                      29:u'主营业务利润（元）',
                      32:u'扣除非经常性损益后的净利润(元)'
                      }
        df = self.df[columns]
        # 调整日期显示
        df.index = df.index.map(lambda x: x[2:7])
        # 处理数据
        for i in columns:
            df[i] = df[i].map(lambda x:0 if x=='--' else float(x))
        figure = plt.figure(22, facecolor='lightgrey')
        plt.suptitle(u'%s盈利能力分析'%self.stockId, fontsize='xx-large', color='gray', alpha=0.4)
        for i in columns:
            ax = figure.add_subplot(2,2,columns.index(i)+1)
            ax.plot(df[i], alpha=0.8)
            ax.set_xticklabels(df.index, rotation=90, fontsize='xx-small')
            plt.title(titles[i], fontsize='small')
        self.__mark_pic(plt, ct.AUTHOR)
        plt.savefig(st.PIC_STOCK%(self.stockId, ct.FINANCIAL_TABLE['profit']), dpi=200)
        return st.PIC_STOCK%(self.stockId, ct.FINANCIAL_TABLE['profit'])

    def analyze_profit_rate_by_year(self):
        """
        按照年度分析股票的盈利能力：
        23. 毛利率、
        17. 营业利润率、
        19. 净利率
        31. 净资产收益率、
        15. 总资产收益率
        :return:
        """
        by_year = [(ct.Q4 % year) for year in range(self.start, self.end + 1)]
        columns = [23,17,19,31,15]
        titles={23:u'毛利率(%)',
                17:u'营业利润率(%)',
                19:u'净利率(%)',
                31:u'净资产收益率(%)',
                15:u'总资产收益率(%)'}
        df = self.df[columns]
        df = df[df.index.isin(by_year)]

        for i in columns:
            df[i] = df[i].map(lambda x:0 if x=='--' else float(x))
        #print(df)
        figure,(ax1,ax2) = plt.subplots(2, 1)
        # 图一：毛利率、营业利润率以及净利率历史分析
        ax1.plot(df[[columns[0],columns[1],columns[2]]], alpha=0.8)
        ax1.legend([titles[columns[0]], titles[columns[1]], titles[columns[2]]])
        ax1.set_xticklabels(df.index.map(lambda x: x[0:4]))
        # 图二：净资产收益率、总资产收益率历史分析
        ax2.plot(df[[columns[3], columns[4]]], alpha=0.8)
        ax2.legend([titles[columns[3]], titles[columns[4]]])
        ax2.set_xticklabels(df.index.map(lambda x:x[0:4]))
        plt.savefig(st.PIC_STOCK % (self.stockId, ct.FINANCIAL_TABLE['profit-tang']), dpi=200)
        return st.PIC_STOCK % (self.stockId, ct.FINANCIAL_TABLE['profit-tang'])

class ManagementTable:
    """
    营运能力报表
    """
    def __init__(self, stockId, start=2008, end=2018):
        """
        :param stockId:
        :param start:
        :param end:
        :return:
        """
        self.stockId = stockId
        self.start = start
        self.end = end
        self.df = investment.load_stock_financial(stockId, '%d-01-01'%start, '%d-12-31'%end)

    def __mark_pic(self,plt, text):
        plt.tight_layout(pad=0.3, w_pad=0.4, h_pad=1.0)
        plt.text(0.75, 0.45, text, rotation=15,
                 fontsize=30, color='lightcoral',
                 ha='center', va='center', alpha=0.4)
    def analyze_by_year(self):
        """

        :return:
        """
        columns = [39,42,66]
        titles = {39:u'应收账款周转率(次)',
                  42:u'存货周转率(次)',
                  66:u'资产负债率(%)'}
        df = self.df[columns]
        df.index = df.index.map(lambda x: x[2:7])
        for i in columns:
            df[i] = df[i].map(lambda x:0 if x=='--' else float(x))
        figure = plt.figure(22, facecolor='lightgrey')
        plt.suptitle(u'%s营运能力分析'%self.stockId, fontsize='xx-large', color='gray', alpha=0.4)
        for i in columns:
            ax = figure.add_subplot(2,2,columns.index(i)+1)
            ax.plot(df[i], alpha=0.8)
            ax.set_xticklabels(df.index, rotation=90, fontsize='xx-small')
            plt.title(titles[i], fontsize='small')
        self.__mark_pic(plt, ct.AUTHOR)
        plt.savefig(st.PIC_STOCK%(self.stockId, ct.FINANCIAL_TABLE['manage']), dpi=200)
        return st.PIC_STOCK%(self.stockId, ct.FINANCIAL_TABLE['manage'])

class BalanceSheet:
    """
    资产负债表
    """
    def __init__(self, stockId, start=2008, end=2018):
        """

        :param stock:
        :param start:
        :param end:
        """
        self.stockId = stockId
        self.start = start
        self.end = end
        self.df = investment.load_stock_accountant_sheet(stockId, 'zcfzb', '%d-01-01'%start, '%d-12-31'%end)

    def analyze_currency_by_year(self):
        """
        按照年度分析货币资金、流动资产、净资产、负债合计的历史趋势
        :return:
        """
        by_year = [(ct.Q4 % year) for year in range(self.start, self.end + 1)]
        columns = [0, 24, 106, 93]
        titles = [u'货币资金(万元)', u'流动资产合计(万元)', u'净资产(万元)', u'负债合计(万元)']
        df = self.df[columns]
        df = df[df.index.isin(by_year)]

        for i in columns:
            df[i] = df[i].map(lambda x:0 if x=='--' else float(x))
        figure,(ax) = plt.subplots(1, 1)
        plt.title(u'%s货币资金变化' % self.stockId, fontsize='large')
        #ax = figure.add_subplot(1,1,1)
        ax.plot(df[[columns[0],columns[1],columns[2],columns[3]]], alpha=0.8)
        ax.set_xticklabels(df.index.map(lambda x : x[0:4]), rotation=30)
        ax.legend(titles)

        plt.savefig(st.PIC_STOCK%(self.stockId, ct.FINANCIAL_TABLE['currency']), dpi=200)
        return st.PIC_STOCK%(self.stockId, ct.FINANCIAL_TABLE['currency'])

    def _get_liability_with_interest(self):
        """
        计算有息负债，暂且计算如下：
        有息负债≈负债合计-应付账款-预收账款-应付职工薪酬-应交税费-长期递延收益-递延所得税负债
        :return:
        """
        by_year = [(ct.Q4 % year) for year in range(self.start, self.end + 1)]
        columns = [59, 60, 63, 64, 89, 90, 93]
        df = self.df[columns]
        df = df[df.index.isin(by_year)]
        for i in columns:
            df[i] = df[i].map(lambda x:0 if x=='--' else float(x))
        df[u'有息负债'] = df[93]-df[59]-df[60]-df[63]-df[64]-df[89]-df[90]
        return df[u'有息负债']

    def _get_productive_assets(self):
        """
        计算生产资产，暂且计算如下：
        生产资产 = 固定资产+在建工程+工程物资+无形资产(土地)
        :return:
        """
        by_year = [(ct.Q4 % year) for year in range(self.start, self.end + 1)]
        columns = [36, 37, 38, 43]
        df = self.df[columns]
        df = df[df.index.isin(by_year)]
        for i in columns:
            df[i] = df[i].map(lambda x: 0 if x == '--' else float(x))
        df[u'生产资产'] = df[36] + df[37] + df[38] + df[43]
        return df[u'生产资产']

    def _get_receivable(self):
        """
        计算含有应收的科目
        应收=
        应收票据+应收账款+应收保费+应收分保账款+应收分保合同准备金+应收利息+
        应收股利+其他应收款+应收出口退税+应收补贴款+应收保证金+内部应收款
        :return:
        """
        by_year = [(ct.Q4 % year) for year in range(self.start, self.end + 1)]
        columns = [5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        df = self.df[columns]
        df = df[df.index.isin(by_year)]
        for i in columns:
            df[i] = df[i].map(lambda x: 0 if x == '--' else float(x))

        df[u'应收'] = df[5]+df[6]+df[8]+df[9]+df[10]+df[11]\
                    +df[12]+df[13]+df[14]+df[15]+df[16]+df[17]
        return df[u'应收']

    def quick_analyze(self):
        """
        资产负债表快速分析
        0:货币资金
        107:总资产
        :return:DataFrame
                'A':u'有息负债/总资产',
                'B':u'生产资产/总资产',
                'C':u'当前税前利润总额/生产资产',
                'D':u'应收/总资产',
                'E':u'货币资金/有息负债',
                'F':u'非主业资产/总资产'
        """
        by_year = [(ct.Q4 % year) for year in range(self.start, self.end + 1)]
        columns = [0, 107]
        df = self.df[columns]
        df = df[df.index.isin(by_year)]
        for i in columns:
            df[i] = df[i].map(lambda x: 0 if x == '--' else float(x))
        df[ct.PROFITSTATEMENT['A']] = self._get_liability_with_interest()/df[107]*100
        df[ct.PROFITSTATEMENT['B']] = self._get_productive_assets()/df[107]*100
        df[ct.PROFITSTATEMENT['C']] = ProfitStatement(self.stockId)._get_profit_before_tax() / \
                                        self._get_productive_assets() * 100
        df[ct.PROFITSTATEMENT['D']] = self._get_receivable()/df[107] * 100
        df[ct.PROFITSTATEMENT['E']] = df[0] / df[107] * 100

        result = [ct.PROFITSTATEMENT['A'], ct.PROFITSTATEMENT['B'],
                   ct.PROFITSTATEMENT['C'], ct.PROFITSTATEMENT['D'],
                   ct.PROFITSTATEMENT['E']]
        for i in result: df[i] = df[i].map(lambda x:'%.2f'%x)

        df[result] = df[result].apply(pd.to_numeric)
        '''
        figure, (ax1) = plt.subplots(1,1)
        ax1.plot(df[u'有息负债/总资产'], alpha=0.8)
        ax1.set_xticklabels(df.index.map(lambda x: x[0:4]))
        plt.title(u'%s有息负债/总资产(百分比)'%self.stockId)
        plt.show()
        '''
        return df[result]

class CashFlowStatement:
    """
    现金流量表
    """
    def __init__(self, stockId, start=2008, end=2018):
        """

        :param stock:
        :param start:
        :param end:
        """
        self.stockId = stockId
        self.start = start
        self.end = end
        self.df = investment.load_stock_accountant_sheet(stockId, 'xjllb', '%d-01-01'%start, '%d-12-31'%end)

    def analyze_cashflow_by_year(self):
        """

        :return:
        """
        by_year = [(ct.Q4 % year) for year in range(self.start, self.end+1)]
        columns = [24, 56, 0, 84, 38, 47]
        titles = {24:u'经营活动产生的现金流量净额(万元)',
                  56:u'净利润(万元)',
                  0:u'销售商品、提供劳务收到的现金(万元)',
                  84:u'现金的期末余额(万元)',
                  38:u'投资活动现金流出小计(万元)',
                  47:u'分配股利、利润或偿付利息所支付的现金(万元)'}
        df = self.df[columns]
        df = df[df.index.isin(by_year)]

        for i in columns:
            df[i] = df[i].map(lambda x:0 if x=='--' else float(x))
        #print(df)
        figure,(ax1,ax2,ax3) = plt.subplots(3,1)
        #plt.title(u'%s现金流量表分析'%self.stockId, fontsize='large')
        ax1.plot(df[[columns[0],columns[1]]], alpha=0.8)
        ax1.legend([titles[columns[0]], titles[columns[1]]])
        ax1.set_xticks([])
        ax2.plot(df[[columns[2]]], alpha=0.8)
        ax2.legend([titles[columns[2]]])
        ax2.set_xticks([])
        ax3.plot(df[[columns[3],columns[4],columns[5]]], alpha=0.8)
        ax3.legend([titles[columns[3]], titles[columns[4]], titles[columns[5]]])
        ax3.set_xticklabels(df.index.map(lambda x : x[0:4]))
        plt.savefig(st.PIC_STOCK%(self.stockId, ct.FINANCIAL_TABLE['cashflow']), dpi=200)
        return st.PIC_STOCK%(self.stockId, ct.FINANCIAL_TABLE['cashflow'])

class ProfitStatement:
    """
    利润表
    """
    def __init__(self, stockId, start=2008, end=2018):
        """

        :param stock:
        :param start:
        :param end:
        """
        self.stockId = stockId
        self.start = start
        self.end = end
        self.df = investment.load_stock_accountant_sheet(stockId, 'lrb', '%d-01-01'%start, '%d-12-31'%end)

    def _get_profit_before_tax(self):
        """
        税前利润总额
        :return:
        """
        by_year = [(ct.Q4 % year) for year in range(self.start, self.end + 1)]
        columns = [36]
        df = self.df[columns]
        df = df[df.index.isin(by_year)]
        for i in columns:
            df[i] = df[i].map(lambda x: 0 if x == '--' else float(x))
        return df[36]

    def quick_analyze(self):
        """
        利润表快速分析
        :return:DataFrame
        """
        new_df = pd.DataFrame()
        columns = [1, 8, 32, 39]
        df = self.df[columns]
        df = df.apply(pd.to_numeric)
        #for i in columns:
        #    df[i] = df[i].map(lambda x: 0 if x == '--' else float(x))
        new_df[u'毛利率'] = (df[1] - df[8]) / df[1] * 100
        new_df[u'净利率'] = df[39] / df[1] * 100
        new_df[u'营业收入增长率'] = [((df[1][i] - df[1][i-4]) / df[1][i-4] * 100) for i in range(len(df[1]))]
        new_df[u'营业利润增长率'] = [((df[32][i] - df[32][i-4]) / df[32][i-4] * 100) for i in range(len(df[32]))]
        return new_df
