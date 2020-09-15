# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:34:54 2020

@author: Jbrown
"""

#Module 4 Homework

line = int(input())

for i in range(0, line):
    twoValues = input().split(' ')
    try:
        print(int(int(twoValues[0])/int(twoValues[1])))
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: '$'")