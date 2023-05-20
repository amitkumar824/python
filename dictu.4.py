# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
def maximum(n1,n2,n3):
    if(n1>n2):
        if(n1>n3):
            print( n1, +"is greatest number")
        else:
            print(n3,+"is graetest number")
    
    else:
        if(n2>n3):
            print( n2, "is greatest number")
        else:
            print(n3, "is graetest number")