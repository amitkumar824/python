# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""

l_main=[]
size=int(input("Enter length of the list: "))
for i in range(1,size+1):
    new= int(input("Enter element no. "+ str(i)+": "))
    l_main+= [new]
print(l_main)


