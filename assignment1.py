# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 00:40:23 2019

@author: Sai Teja
"""
population={"shanghai":17.8,"istanbul":13.3,"karachi":13.0,"mumbai":12.5}
print(population)

animals={'dogs':[20,10,15,8,32,15],'cats':[3,4,2,8,2,4],'rabbits':[2,3,3],'fish':[0,3,0.5,0.8,0.3,1]}
print(animals['dogs'])
print(animals['dogs'][3])
print(animals['fish'])

a=[1,2,2,3,3,3,4,4,4,4]
b=set(a)
print(b)
print(len(a))
print(len(b))
len(a)-len(b)
print(len(a)-len(b))

tuple_a=3,4
tuple_b=(3,4)
print(tuple_a)
print(tuple_b)
print(tuple_a==tuple_b)
print(tuple_a[1])

names=["carol","albert","ben","donna"]
print("&".join(sorted(names)))

names=["carol","albert","ben","donna"]
print("&".join(names))

names=["carol","albert","ben","donna"]
sorted(names)
print("&".join(sorted(names)))