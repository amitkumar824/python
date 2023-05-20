# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""

l=list(int(input()))
i=0 
z=len(l) 
while i<z: 
       if l[i]<0 or l[i]%2!=0:
              l.remove(l[i])
              z=z-1
       else:
              i=i+1
print(l)
