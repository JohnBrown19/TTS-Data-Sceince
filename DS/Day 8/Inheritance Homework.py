# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:51:59 2020

@author: infer
"""
#import numpy as np
class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
class Student(Person):
    def __init__(self, firstname, lastname, ID, grades):
        self.ID = ID
        self.grades = grades
        self.avg = 'not calculated'
        super().__init__(firstname, lastname)
        
    def __str__(self):
        #return str(self.firstname, self.lastname, self.ID, self.grades, self.avg)
        return (self.firstname + " " + self.lastname + " " + str(self.ID) + " " + str(self.grades))
#return (self.firstname + " " + self.lastname + " " + str(self.ID) + " " + str(self.grades))

    def calculate(self):
        #self.avg = sum(int(self.grades))/len(int(self.grades))
        self.grades = list(map(int, self.grades))
        self.avg = sum(self.grades)/len(self.grades)
    
        
        if self.avg >= 90:
            #print('A')
            return('A')
            #could set prints as returns to use the testing code
        elif self.avg < 90 and self.avg >= 80:
            #print('B')
            return('B')
        elif self.avg >= 70 and self.avg < 80:
            #print('C')
            return('C')
        elif self.avg >= 60  and self.avg < 70:
            #print('D')
            return('D')
        else: #self.avg < 60:
            #print('F')
            return('F')
            
listOfStudents = []
cont = "y"
while(cont == "y"):
    listOfStudents.append(Student(input("First name:"), input("Last name:"), input(
        "ID:"), input("Scores(ENTER AS A SPACE SEPARATED LIST):").split()))
    cont = input("Add another student?(y/n)")
for i in listOfStudents:
    print(str(i) + " " + i.calculate())
    #i.calculate()

        
    