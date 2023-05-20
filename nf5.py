# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
a= int(input("Enter the number"))

factorial =1
    
for i in range(1,a+1):
    factorial = factorial*i
    
print(factorial)