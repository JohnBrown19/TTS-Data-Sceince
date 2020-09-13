# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 01:09:26 2020

@author: Jbrown
"""

#y = ax^2 + bx + c
#x = (-b+-(b**2-4ac)**(1/2))/(2a)
def solve_quadratic (a, b, c):
    x1 = (-b + (b**2-4*a*c)**(1/2))/(2*a)
    x2 = (-b - (b**2-4*a*c)**(1/2))/(2*a)
    return(x1, x2)
    