# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Module 2 exercises

#1
#import math
def solve_quadratic(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**(1/2))/(2*a)
    return (x1, x2)

#2
#user_list = input("Please type a space-seperated list of integers to hash: ")
#print(hash(tuple(user_list[::2])))

#3
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = []
listThree = listOne[1::2]
listThree += listTwo[::2]
#listThree.append(listOne[1::2])
#listThree.append(listTwo[::2])


#4
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
firstList = sampleList[0:3]
secondList = sampleList[3:6]
thirdList = sampleList[6:9]
print(firstList[::-1])
print(secondList[::-1])
print(thirdList[::-1])

#5
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Zach':47, 'Emma':69, 'Kelly':76, 'Jason':97}
removeList = []
for value in rollNumber:
    if value not in sampleDict.values():
        removeList.append(value)
for rm_value in removeList:
    rollNumber.remove(rm_value)
print(rollNumber)
