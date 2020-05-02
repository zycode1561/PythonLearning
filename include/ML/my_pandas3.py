#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:30:03 2020

@author: zhangyun
"""

# Series,DataFrame是又Series组成的，Seriex相当于一行或者一列

import pandas as pd
fandango = pd.read_csv("/Users/zhangyun/Desktop/PythonWorkspace/fandango_score_comparison.csv")

series_film = fandango['FILM']
series_rt = fandango['RottenTomatoes']
film_names = series_film.values

