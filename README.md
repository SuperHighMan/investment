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

### 截至2018年4月19日A股市盈率计算完毕
```commandline
(pyenv3.6) [chenhui@test-os-7 investment]$ cat logs/20180419-pe-ttm.out |grep '出错'|wc -l
394
(pyenv3.6) [chenhui@test-os-7 investment]$ ll -lrt data/stock_pe_ttm/|wc -l
3119
```

## 问题
绘制股价市盈率图与股价时，是否采用前复权的股价，目前为不复权的价格？？

## 附:url
---------------------------------------
```angular2html
# 市场指数url e.g.中证环保
http://quotes.money.163.com/service/chddata.html?code=0000827&start=20120104&end=20180413&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER 
http://quotes.money.163.com/service/chddata.html?code=0000905&start=20050104&end=20180413&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER 
http://quotes.money.163.com/service/chddata.html?code=1399300&start=20020104&end=20180413&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER 
```

## 分析图
--------------------
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