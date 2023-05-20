# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
str_main= input("Enter the string: ")
sum,digs=0,''
for i in str_main:
    if i.isdigit():
        digs+=i
        sum+=int(i)
if sum>0:
    print(str_main,'has digits',digs,'which sum to',sum)
else:
    print("Given string has no digits")