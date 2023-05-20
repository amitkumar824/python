# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""

d={} 
n=int(input("Enter len of the dict.: ")) 
for i in range(n): 
       h=eval(input("Enter the key: ")) 
       k=eval(input("Enter the value: ")) 
       d[h]=k 
print(d)
