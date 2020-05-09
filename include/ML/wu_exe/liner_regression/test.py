#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Zy_Code'

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, 'r')

fig, ax2 = plt.subplots(figsize=(8, 6))
z1 = -np.log(y)
z2 = -np.log(1 - y)
ax2.plot(y, z1, label='y == 1')
ax2.plot(y, z2, label='y == 0')
ax2.legend(loc='best')
plt.show()
