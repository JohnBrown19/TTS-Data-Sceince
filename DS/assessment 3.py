# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 03:55:18 2020

@author: infer
"""

#Homewokr #4
#hackerrank exercise 1

def is_leap(year):
    leap = False
    if (year % 4 == 0):
        leap  = True
    if year % 100 == 0:
        leap = False
        if year % 400 == 0:
            leap = True

    return leap

year = int(input())

#hackerrank exercsie 2

lines = int(input())

for i in range(0, lines):
    lineSplit = input().split(' ')
    try:
        print(int(int(lineSplit[0])/int(lineSplit[1])))
    except ZeroDivisionError:
        print("Error Code: Integer division or modulo by zero")
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: '$'")