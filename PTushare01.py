# -*- coding: utf-8 -*-

'''
Created on 2019年7月31日

@author: qiao.gu
'''
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import pandas as pd
import tushare as ts
from calendar import month
print(ts.__version__)
# df = ts.get_hist_data('600570')
# print(ts.get_hist_data('600570'))
# df.to_excel('D:\恒生电子.')
# 复权数据
# print(ts.get_h_data('600570'))
# 限售股解禁
# print(ts.xsg_data(year=2019,month=7))
# 行业分类
# templ = ts.get_industry_classified()
# print(templ)
# print(templ.loc[templ['c_name']=='综合行业'])
# 保存进Excel
# 2019-7-31 行情数据
# D:\20190731_行情数据

# # 写数据到数据库中
# # 连接MySQL数据库，把数据导入到数据库中 
# df = ts.get_today_all()
# engine = create_engine('mysql://root:K@ppy213@localhost/sjfx?charset=utf8')
# # print(df)
# 
# #存入数据库 
# df.to_sql('today_all_data',engine)
basic = ts.get_stock_basics()
print(basic)