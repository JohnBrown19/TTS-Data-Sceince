# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:15:06 2020

@author: infer
"""

#import email.utils
#print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
#print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))

#import email.utils
import re
#each bracket is just one character

lines = input()
validEmail = re.compile(r'<[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>')

for x in range(int(lines)):
    name, emailAddress = input().split()
    if validEmail.match(emailAddress):
        print(name, emailAddress)