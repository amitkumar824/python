# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:30:25 2023

@author: hp
"""
import numpy as np

# Create a one-dimensional NumPy array
x = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array into a two-dimensional matrix with 2 rows and 3 columns
x_matrix = np.reshape(x, (2, 3))

# Print the resulting matrix
print(x_matrix)
