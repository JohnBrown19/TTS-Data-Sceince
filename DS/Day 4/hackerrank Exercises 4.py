# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:01:53 2020

@author: Jbrown
"""

#Exercise 1

def is_leap_year(year):
    leap = False
    if (year % 4 == 0):
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap
year = int(input())

#Exercise 2

lines = int(input())

for i in range(0, lines):
    lineSplit = input().split(' ')
    try:
        print(int(int(lineSplit[0])//int(lineSplit[1])))
        #or use:
        #X, Y = map(int, lineSplit)
        #print(X//Y)
    except ZeroDivisionError as m:
        print("Error Code:", m)
    except ValueError as m:
        print("Error Code:", m)
