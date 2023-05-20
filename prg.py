# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
p_num=input("Enter the phone number: ")
p_dash= p_num[3] + p_num[7]
p_dig= p_num[:3] + p_num[4:7] + p_num[8:]
if len(p_num)== 12 and p_dash=="--" and p_dig.isdigit():
    print("Given phone number is valid")
else:
    print("Given phone number is invalid")