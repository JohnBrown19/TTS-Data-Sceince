# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:35:30 2020

@author: Jbrown
"""

import random
import string
import re
#Exercise #4
#Check attendance for 75% or less
#use input()

# classes_held = int(input("How many classes are held (Integer): "))
# classes_attended = int(input("How many classes did they attend (Integer): "))
# percent_attended = float(classes_attended/classes_held)
# print(percent_attended)

# if percent_attended < 0.75:
#     print("Student cannot sit in the exam.")
# else:
#     print("Student may sit in the exam.")
    
#1
#Guess a number between 1 and 9
    
# guess = int(input("Give us a number between one and nine: "))
# our_guess = random.randint(1, 9)

# if our_guess == guess:
#     print("We guessed that your number was " + str(guess) + "!")
# else:
#     print("Sorry. your number was " + str(guess) + " and we guessed " + str(our_guess) + ".")
    
"""Alt. way from instructor 
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('You guessed correct!')
"""

#2
# validPword = input("Please input a valid password: ")
# upper = string.ascii_uppercase
# lower = string.ascii_lowercase
# specChar = '#$@'
# numbers = '0123456789'
# length = len(validPword)

# verify_upper = 0
# verify_lower = 0
# verify_char = 0
# verify_num = 0
# verify_length = 0
# #verify = verify_upper + verify_lower + verify_char + verify_num + verify_length

# #while verify < 5:
# for i in validPword:
#     if i in upper:
#         verify_upper = 1
#     if i in lower:
#         verify_lower = 1
#     if i in specChar:
#         verify_char = 1
#     if i in numbers:
#         verify_num = 1
#     if 6 <= length <= 16:
#         verify_length = 1
# verify = verify_upper + verify_lower + verify_char + verify_num + verify_length
# if verify < 5:
#     print("Sorry. This is not a valid password. Try again. ")
#     #validPword = input("Please input a valid password: ")
# else:
#     print("This is a valid password!")

            
    
#2
password = input("Please input your password: ")
valid = True
while valid:
    if (len(password) < 6 or len(password) > 16):
        print("Password is not between 6 adn 16 characters. Try again.")
        password = input("Please input your password: ")
        break
    elif not re.search("[a-z]", password):
        print("Password missing at least one lowercase letter. Try again.")
        password = input("Please input your password: ")
        break
    elif not re.search("[A-Z]", password):
        print("Password missing at least one uppercase letter. Try again.")
        password = input("Please input your password: ")
        break
    elif not re.search("[0-9]", password):
        print("Password missing at least one number. Try again.")
        password = input("Please input your password: ")
        break
    elif not re.search("[$#@]", password):
        print("Password missing at least one special character. Try again.")
        password = input("Please input your password: ")
        break
    else:
        print("This is a valid password.")
        x = False
        break

#4

