# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:11:15 2020

@author: infer
"""
import random
import string
#import re
#1
userGuess = int(input("Pick a number between 1 and 9 for us to guess:"))
ourGuess = random.randint(1, 9)
if userGuess == ourGuess:
    print("Aha! we guess your number " + str(userGuess) + "!")
else:
    print("Alas! we guessed " + str(ourGuess) + ", but your number was " + str(userGuess) + ".")
#2
# userPword = list(input("Please input a valid password: "))
# if len(userPword) < 6 or len(userPword) > 16:
#     print("not a valid password length. Makre sure the password is between 6 adn 16 characters")
#     userPword = list(input("Please input a valid password: "))
    
#3
# userAges = input("Give us the names, ages of three uses to see who is the oldest and youngest among them: ")
# userAges = list(userAges.split())
# userDict = {}
# #userDict.append(userAges.keys(userAges[::2]))
# for i in range(0, len(userAges), 2):
#     userDict[userAges[i]] = userAges[i+1]
# #print(userDict)
# sortedDict = sorted(userDict.items(), key=lambda x: x[1], reverse=True)
# print(str(sortedDict[0]) + " is the oldest.")
# print(str(sortedDict[-1]) + " is the youngest.")
#4
# classesHeld = int(input("How many classes are held (Integer): "))
# classesAttended = int(input("How many classes did they attend (Integer): "))
# attendancePercent = float(classesAttended/classesHeld)
# print("attendance percentage = " + str(attendancePercent*100) + "%")
# if attendancePercent < 0.75:
#     print("The student cannot sit for the exam.")
#else:
#    print("The student can sit for the exam.")
#5
# userInteger = int(input("please input an integer, N to see if it is weird: "))
# if userInteger % 2 != 0:
#     print("weird")
# elif userInteger in range(2,6) and userInteger % 2 == 0:
#     print("Not weird")
# elif userInteger % 2 == 0 and userInteger in range(6, 21):
#     print("weird")
# elif userInteger % 2 == 0 and userInteger > 20:
#     print("Not weird")


# validPword = False
# while validPword == False:
#     userPword = input("Please input a valid password: ")
#     if len(userPword) < 6 or len(userPword) > 16:
#         print("not a valid password length. Makre sure the password is between 6 and 16 characters")
#         #userPword = input("Please input a valid password: ")
    
#     else:
#         print("This is a valid password")
#         validPword = True


#2 
#upper = string.ascii_uppercase
#lower = string.ascii_lowercase
#numbers = '0123456789'
#char = " """