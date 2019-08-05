'''
Created on 2019年8月2日

@author: qiao.gu
'''
import tushare as ts
import pandas as pd

path='D:/Personal_Workspace/P-Test/PythonTest/src/PTushareTest/today_all.xlxs'

def get_all_data():
    df=ts.get_today_all()
    print(df)
    
if __name__ == '__main__':
    get_all_data()