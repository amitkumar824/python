# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
a = int(input('enter 1st number'))
b =int(input('enter 2nd number'))

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)