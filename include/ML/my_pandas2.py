#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:25:10 2020

@author: zhangyun
"""

import pandas as pd
import numpy as np

titanic_survival = pd.read_csv("/Users/zhangyun/Desktop/PythonWorkspace/titanic_train.csv")

age = titanic_survival["Age"]

age_is_null = pd.isnull(age)
age_null_true = age[age_is_null]
age_null_count = len(age_null_true)

good_ages = titanic_survival["Age"][age_is_null == False]

correct_mean_age = sum(good_ages) / len(good_ages)

# 上面的求均值也可以直接使用 titanic_survival["Age"].mean()完成

# 通过Pclass进行分组，计算Survived的mean值，也就是均值
passenger_survival = titanic_survival.pivot_table(index = "Pclass", values="Survived", aggfunc=np.mean)

#aggfunc不写默认求均值
passenger_age = titanic_survival.pivot_table(index = "Pclass", values="Age")

port_stats = titanic_survival.pivot_table(index = "Embarked",values=["Fare", "Survived"], aggfunc = np.sum)

# 如果列中有缺失值，直接就丢掉样本
drop_na_cloumns = titanic_survival.dropna(axis=1)

# 如果Age列和Sex列含有NaN值，就会把这一行丢掉
new_titanic_survival = titanic_survival.dropna(axis=0, subset=["Age","Cabin"])

#定位到具体位置的数据
row_index_83_age = titanic_survival.loc[6,"Age"]

sort = titanic_survival.sort_values("Age", ascending=False)
#重新给index进行排序
titanic_reindexed = sort.reset_index(drop=True)\

def hundredth_row(column):
    hundredth_item = column.loc[99]
    return hundredth_item

hundredth_row = titanic_survival.apply(hundredth_row)



