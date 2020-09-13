# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 23:37:09 2020

@author: Jbrown
"""

#sorting 2 number arrays
import numpy as np
a1 = np.array([0, 2, 4, 6, 7])
a2 = np.array([1, 3, 4, 5, 7])
#a1_index = 0
#a2_index = 0
#final_array = []

def merge_array(x, y):
    a1_index = 0
    a2_index = 0
    final_array = []
    # for index in x, y:
    for index in range(len(x) + len(y) - 2):
            if x[a1_index] < y[a2_index]:
                final_array.append(x[a1_index])
                a1_index += 1
            elif x[a1_index] == y[a2_index]:
                final_array.append(y[a2_index])
                final_array.append(x[a1_index])
                a1_index += 1
                a2_index += 1
            else:
                final_array.append(y[a2_index])
                a2_index += 1
    return np.array(final_array)

# def merge_array(x, y):
#     for a in x:
#         for b in y:
#             if a < b:
#                 final_array.append(a)
#             elif a == b:
#                 final_array.append(b)
#             else:
#                 final_array.append(a)
#     return np.array(final_array)