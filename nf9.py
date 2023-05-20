# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
a=int(input("Enter the marks of first subject :"))
b=int(input("Enter the marks of second subject :"))
c=int(input("Enter the marks of third subject :"))


if(a<33 or b<33 or c<33):
    print("Fail")
    
elif((a+b+c)/3 <40 ):
    print("Fail")
else:
    print("Paas")