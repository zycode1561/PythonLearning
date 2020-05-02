#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:44:34 2020

@author: zhangyun
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
unrate = pd.read_csv("/Users/zhangyun/Desktop/PythonWorkspace/UNRATE.csv")
unrate['DATE'] = pd.to_datetime(unrate['DATE'])


first_twelve = unrate[0:12]
plt.plot(first_twelve['DATE'],first_twelve['VALUE'],c='red')
plt.xticks(rotation=45) # 指定x轴倾斜角度
plt.xlabel('Month') #指定x轴的单位
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948') # 指定图像标题
plt.show()

fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(3,2,1) # 子图，表示四行三列矩阵的第一个
ax2 = fig.add_subplot(3,2,2)
ax3 = fig.add_subplot(3,2,3)
ax1.plot(np.random.randint(1,5,5), np.arange(5))
ax2.plot(np.arange(10)*3, np.arange(10))


unrate['MONTH'] = unrate['DATE'].dt.month
ax4 = fig.add_subplot(3,2,4)
ax4.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'],c='red',label=1948)
ax4.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'],c='blue',label=1949)

plt.legend(loc='best')
plt.show()




