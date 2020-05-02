#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:53:12 2020

@author: zhangyun
"""
import pandas
food_info = pandas.read_csv('/Users/zhangyun/Desktop/PythonWorkspace/food_info.csv')

food_info.head(3) # 显示出一个表格，就是读取的数据,参数是显示前几条代码
food_info.tail(3) # 从后往前取
food_info.columns # 获得所有列名
food_info.shape # 显示几行几列

food_info.loc[0] # 获取第n-1个数据,也可以通过切片使用
ndb_col = food_info["NDB_No"]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]

col_names = food_info.columns.tolist()

gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
gram_df = food_info[gram_columns]

div_1000 = food_info["Iron_(mg)"] / 1000

# food_info.sort_values("Sodium_(mg)", inplace=True) # inplace表示是否在原来的基础上生成一个新的DataFrame，True表示在原来的基础上进行排序

v = food_info.sort_values("Sodium_(mg)", inplace=False)

food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False) # 第三个参数表示升序为Flase，也就是采用降序






