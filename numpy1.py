# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
import numpy as np

# Create two one-dimensional NumPy arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Stack the arrays vertically to create a two-dimensional matrix
z = np.vstack((x, y))

# Print the resulting matrix
print(z)
