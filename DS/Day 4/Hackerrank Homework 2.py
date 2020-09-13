# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:27:21 2020

@author: Jbrown
"""

#exception handling
#line = int(input())

# for i in range(0, line):
#     twoValues = input().split(' ')
#     try:
#         print(int(int(twoValues[0])/twoValues[1]))
#     try:
#         print('ya ya ya')
#     except:
#         print('methhead')

a = [1, 2, 3]
b = [2, 5, 5]
c = []
def merge_array(a, b):
    #c = []
    for i in range(0, max(len(a), len(b))):
        c.append(a[i])
        c.append(b[i])
    c.sort()
    #print(c)
    return c