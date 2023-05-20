# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
str_main="Hi! my name is Gaurav"
str_find=input("Enter the word to be searched: ")
cnt=0
for i in str_main:
    if i == str_find:
        cnt+=1
print("The word you searched has appeared",cnt,"times in the line.")