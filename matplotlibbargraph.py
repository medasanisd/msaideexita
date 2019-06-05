# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:36:32 2019

@author: Sai Teja
"""

import numpy as np
import matplotlib.pyplot as plt
x_axis=['a','b','c','d']
y_axis=[2,8,6,9]
index=np.arange(len(x_axis))
index

plt.bar(index,y_axis)
plt.xticks(index+0.5,x_axis)