# investment
---
>关于本项目，本项目属个人分析投资使用，项目主要爬取了A股市场的数据，主要包括
股票和基金数据。截至2018年4月10日，涉及A股市场3511只股票；指数基金976只，
指数QDII基金85只;另外爬取了全市场指数历史数据共记346只。

## 数据来源
新浪财经
网易财经
凤凰财经
天天基金
韭菜说

1. 截至2018年4月19日A股市盈率计算完毕
```
$ cat logs/20180419-pe-ttm.out |grep '出错'|wc -l
394
$ ll -lrt data/stock_pe_ttm/|wc -l
3119
```
2. 截至2018年4月22日A股市净率计算完毕
```
$ cat logs/20180422-pb.out |grep '出错'|wc -l
9
$ ll -lrt data/stock_pb/|wc -l
3503

```

## 问题
1. 绘制股价市盈率图与股价时，是否采用前复权的股价，目前为不复权的价格
2. 分析股票数据时，百分位标记图，百分位pe程度
3. 股票基本面分析

## 一、基本面分析
+ 每股收益(EPS)=净利润/普通股总股数 *财务指标:index\[4\]*
+ 市盈率 普通股每股市价/普通股每股收益 *已完成*
+ 每股净资产 年度末股东权益/年度末普通股数 *财务指标:index\[7\]*
+ 市净率 每股市价/每股净资产 *已完成*
+ 净资产收益率 净利润÷平均净资产 *财务指标:index\[30\]*
+ 利润增长率 (本期净利润-上期净利润)/上期净利润 *财务指标:index\[35\]*
+ 资产负债率 负债总额÷资产总额×100% *财务指标:index\[66\]*
+ 流动比率 流动资产÷流动负债×100% *财务指标:index\[50\]*
+ 速动比率 (流动资产-存货)÷流动负债×100% *财务指标:index\[51\]*
+ 存货周转率 主营业务成本÷平均存货 *财务指标:index\[42\]*
+ 应收账款周转率 主营业务收入÷平均应收账款 *财务指标:index\[39\]*
+ 现金流动负债比 经营现金流量净额/流动负债 *财务指标:index\[72\]*

## 附:url
```
#市场指数url e.g.中证环保
http://quotes.money.163.com/service/chddata.html?code=0000827&start=20120104&end=20180413&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER 
http://quotes.money.163.com/service/chddata.html?code=0000905&start=20050104&end=20180413&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER 
http://quotes.money.163.com/service/chddata.html?code=1399300&start=20020104&end=20180413&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER 
#资产负债表
http://quotes.money.163.com/service/zcfzb_600519.html
#利润表
http://quotes.money.163.com/service/lrb_600519.html
#现金流量表
http://quotes.money.163.com/service/xjllb_600519.html
```



## 分析图
```
季度利润增长趋势图 Q1 Q2 Q3 Q4 继续按年分析
盈利能力 净资产收益率ROE 营业利润 净利润
流动资产合计
现金流
```
## 参考网站
```angular2html
http://www.jiucaishuo.com/
投资数据下载
python分析指数估值图
python爬虫
```