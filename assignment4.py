# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:33:12 2019

@author: Sai Teja
"""

import pandas as pd
stock=[{'year':1990,'name':'alice','dept':'hr','age':25,'salary':50000},
      {'year':1990,'name':'bob','dept':'rd','age':30,'salary':48000},
      {'year':1990,'name':'charlie','dept':'admin','age':45,'salary':55000},
      {'year':1991,'name':'alice','dept':'hr','age':26,'salary':52000},
      {'year':1991,'name':'bob','dept':'rd','age':31,'salary':60000},
      {'year':1991,'name':'charlie','dept':'admin','age':46,'salary':52000},
      {'year':1992,'name':'alice','dept':'admin','age':27,'salary':60000},
      {'year':1992,'name':'bob','dept':'rd','age':32,'salary':52000},
      {'year':1992,'name':'charlie','dept':'admin','age':28,'salary':62000}]
company=pd.DataFrame(stock,index=[0,1,2,3,4,5,6,7,8])
print(company)

company.groupby(['year'])['salary'].sum()

company.groupby(['year','dept'])['salary'].sum()