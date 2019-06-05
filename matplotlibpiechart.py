# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:38:57 2019

@author: Sai Teja
"""

import matplotlib.pyplot as plt
x=[90,50,40,50,60]
plt.pie(x)
plt.show()

labels='ego','love','anger','happy','sad'
plt.pie(x,labels=labels)
plt.show

plt.pie(x,labels=labels,autopct='%1.1f%%')
plt.show()

plt.pie(x,labels=labels,autopct='%1.1f%%',shadow='true')
plt.show()

explode=[.2,.2,0,0,0]
plt.pie(x,explode=explode,labels=labels,autopct='%1.1f%%',shadow='true')
plt.show()

