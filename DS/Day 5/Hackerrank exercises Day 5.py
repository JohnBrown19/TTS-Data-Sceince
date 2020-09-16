# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:13:25 2020

@author: Jbrown
"""
#Exercise 1

from itertools import product
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
XCrossY = product(X, Y)
print(*XCrossY)

#Exercise 2

from itertools import permutations

def Permutations(str, num):
    text = list(permutations(str, num))
    text.sort()
    for i in text:
        print(''.join(i))
        
if __name__ == "__main__":
    str, num = input().split(' ')
    Permutations(str, int(num))

#Exercise 3

from itertools import combinations_with_replacement as cwr

word, num = input().split(' ')
num = int(num)

text = list(cwr(word, num))

combinations = []

for combs in text:
    result = ""
    combs = sorted(combs)
    for i in combs:
        result += i
    combinations.append(result)

combinations.sort()
for combs in combinations:
    print(combs)
    
    
