# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 11:11:15 2020

@author: infer
"""
import random
import re
#1
# userGuess = int(input("Pick a number between 1 and 9 for us to guess:"))
# ourGuess = random.randint(1, 9)
# if userGuess == ourGuess:
#     print("Aha! we guess your number " + str(userGuess) + "!")
# else:
#     print("Alas! we guessed " + str(ourGuess) + ", but your number was " + str(userGuess) + ".")
#2
# password = input("Please input your password: ")
# valid = True
# while valid:
#     if (len(password) < 6 or len(password) > 16):
#         print("Password is not between 6 adn 16 characters. Try again.")
#         password = input("Please input your password: ")
#         break
#     elif not re.search("[a-z]", password):
#         print("Password missing at least one lowercase letter. Try again.")
#         password = input("Please input your password: ")
#         break
#     elif not re.search("[A-Z]", password):
#         print("Password missing at least one uppercase letter. Try again.")
#         password = input("Please input your password: ")
#         break
#     elif not re.search("[0-9]", password):
#         print("Password missing at least one number. Try again.")
#         password = input("Please input your password: ")
#         break
#     elif not re.search("[$#@]", password):
#         print("Password missing at least one special character. Try again.")
#         password = input("Please input your password: ")
#         break
#     else:
#         print("This is a valid password.")
#         x = False
#         break
    
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
