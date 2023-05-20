# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
a= input("Enter the text :  ")

if ("hey" in a):
    spam = True
elif("good morning" in a):
    spam= True
else:
    spam= False
    
if(spam):
    print(" it is spam ")
else:
    print("Not a spam")