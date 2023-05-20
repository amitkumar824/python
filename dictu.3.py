# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
a= int(input("Enter marks:"))


if(90<a and a<100):
    print(" Excellent")
    
elif(80<a and a<90):
    print(" Grade A")


elif(70<a and a<80):
    print(" Grade B")



elif(60<a and a<70):
    print(" Grade C")

elif(50<a and a<60):
    print("Grade D")
    
else:
    print("Grade F")