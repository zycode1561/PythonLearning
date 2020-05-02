#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:49:37 2020

@author: zhangyun
"""

import matplotlib.pyplot as plt
import pandas as pd
reviews = pd.read_csv("/Users/zhangyun/Desktop/PythonWorkspace/fandango_score_comparison.csv")
cols = ['FILM','RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue','Fandango_Stars']
norm_reviews = reviews[cols]

from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue','Fandango_Stars']

bar_heights = norm_reviews.loc[1, num_cols].values
bar_positions = arange(5) + 0.75
fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.4) # 后面的0.3是柱的 宽度 .bar是竖着，.barh是横着
plt.show()

# 散点图 。scatter



