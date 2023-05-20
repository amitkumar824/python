# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
l_main=[23,43,56,24,45,23,44,65,78,45]
l_new=[]
for i in l_main:
    if i not in l_new:
        l_new+= [i]
l_main= l_new
print(l_main)
