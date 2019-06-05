# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 00:50:10 2019

@author: Sai Teja
"""
import numpy as np
x=np.array([1,2,3,4])
y=np.array([5.5,6.5,7.5,8.5])
z=np.add(x,y)
print('z=',z)

import numpy as np
x=np.array([1,2,3,4])
y=np.array([5.5,6.5,7.5,8.5])
z=np.multiply(x,y)
print('z=',z)

import numpy as np
x=np.array([1,2,3,4])
y=np.array([5.5,6.5,7.5,8.5])
z=np.subtract(x,y)
print('z=',z)

import numpy as np
x=np.array([1,2,3,4])
y=np.array([5.5,6.5,7.5,8.5])
z=np.divide(x,y)
print('z=',z)

x=np.array([[1,2],[3,4]])
print('x=',x)
y=np.sqrt(x)
print('y=',y)

x=np.array([[1,2],[3,4]])
print('x=',x)
y=np.min(x,1)
print('y=',y)

y=np.max(x,0)
print('y=',y)

y=np.max(x,1)
print('y=',y)

y=np.std(x)
print('y=',y)

y=np.mean(x)
print('y=',y)

y=np.median(x)
print('y=',y)

y=np.exp(x)
print('y=',y)
