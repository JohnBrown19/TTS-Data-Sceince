# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:54:27 2020

@author: infer
"""

class MyClass(object):
    """Documentation string of the class"""

    def __init__(self, param1, param2):
        "This initialises an instance of type ClassName"
        self.b = param1 # creates an instance attribute
        c = param2      # creates a local variable of the function
        # statements ...

    def f(self, param1):
        """This is a method of the class"""
        # some statements

    a=1 # This creates a class attribute