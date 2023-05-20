# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
def percent(marks):
    p = (marks[0]+marks[1]+marks[2])/3
    return p
    
mark = [67,62,49]
p = percent(mark)
    
print(p)