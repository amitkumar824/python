# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""

l1=[24,69,90,12,65] 
l2=[12,69,9,65,89] 
l3=[] 
for i in l1: 
       if  i in l2: 
              l3=l3+[i] 
print(l3)

