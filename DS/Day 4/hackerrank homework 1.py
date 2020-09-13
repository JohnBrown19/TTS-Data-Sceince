# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:01:53 2020

@author: Jbrown
"""
import numpy as np

leapyear = np.arange(1900, 10**5, 4)
noleapyear = np.arange(1900, 10**5, 1)   

def is_leap_year(year):
    leap = False
    if (year % 4 == 0):
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap
    
    # if (year % 4 == 0) or (year % 400 == 0) or year
    #     if year % 100 != 0:
    #         (year % 400 == 0):
    # leap = True
    # #elif year % 100 != 0:
    # #    leap = False
    # return leap

    # #year = 
    