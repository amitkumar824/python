# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
Planet = input("Enter planet's name : ")

Date = input("Enter date :")

Letter = Letter.replace("<|Planet|>" , Planet)

Letter =Letter.replace("<|Date|>", Date)

print(Letter)