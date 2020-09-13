# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 01:27:47 2020

@author: Jbrown
"""
#y = ax^2 + bx + c
#x = (-b+-(b**2-4ac)**(1/2))/(2a)
def solve_quadratic (a, b, c):
    x1 = (-b + (b**2-4*a*c)**(1/2))/(2*a)
    x2 = (-b - (b**2-4*a*c)**(1/2))/(2*a)
    return(x1, x2)
    
#newtuple = tuple(input("list of integers").split())
#print(hash(newtuple))
#It is seeing the numbers as a string, which is why/
#the hash is negative


listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
list3 = listOne[1::2]
list3 += listTwo[::2]

L = [11, 45, 8, 23, 14, 12, 78, 45, 89]
L1 = L[0:3]
L2 = L[3:6]
L3 = L[6:]
print(L1[::-1])
print(L2[::-1])
print(L3[::-1])

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Zach':47, 'Emma':69, 'Kelly':76, 'Jason':97}

tracking = []
for i in rollNumber:
    if i not in sampleDict.values():
        tracking.append(i)
for j in tracking:
    if j in rollNumber:
        rollNumber.remove(j)
print(rollNumber)







