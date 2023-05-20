# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
p=int(input("Enter principal amount:"))
t=int(input("Enter time period (in years) :"))
r=float(input("Enter rate of interest:"))
simpleInterest=(p*t*r)/100
print("Simple interest is:",simpleInterest)