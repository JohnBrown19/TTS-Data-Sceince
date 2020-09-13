# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:40:32 2020

@author: Jbrown
"""

#Talking about control flow

#if-elif-else, 
#for-loops and while loops
#break, continue, pass, etc. 

#if-elif-else
x = 0

if x == 0:
    print(x, "is zero")
elif x > 0:
    print(x, "is positive")
elif x < 0:
    print(x, "is negative")
else:
    print(x, "is unlike anything I've ever seen...")
    
#for, use for a set amount of iterations
for N in [2, 3, 5, 7]:
    print(N, end=' ') # print all on same line
    
#while, for an unknown amount of iterations
i = 0
while i < 10:
    print(i, end=' ')
    i += 1

#continue, skips rest of code, and goes to next iteration
for n in range(20):
    # if the remainder of n / 2 is 0, skip the rest of the loop
    if n % 2 == 0:
        continue
    print(n, end=' ')
    
#break, stops the whole code from procedding further
a, b = 0, 1
amax = 100
L = []

while True:
    (a, b) = (b, a + b)
    if a > amax:
        break
    L.append(a)

print(L)

#Loops with else block
L = []
nmax = 30

for n in range(2, nmax):
    for factor in L:
        if n % factor == 0:
            break
    else: # no break
        L.append(n)
print(L)

#example1
#x=input("Give an integer: ")
x=int(x)
if x >= 0:
    a=x
else:
    a=-x
#print("The absolute value of %i is %i" % (x, a))

#example2
"""c=float(input("Give a number: "))
if c > 0:
    print("c is positive")
elif c<0:
    print("c is negative")
else:
    print("c is zero")"""

#example3
l=[1,3,65,3,-1,56,-10]
for x in l:
    if x < 0:
        break
#print("The first negative list element was", x)

#functions
def double(x):
    "This function multiplies its argument by two."
    return x*2

#def sum_of_squares(*t):
    #*t =  argument packing, to allow for multiple arguments
    #there is also an unacking feature

# def sum_of_squares(a, b):
#     "Computes the sum of arguments squared"
#     return a**2 + b**2

def sum_of_squares(*lst):
    "Computes the sum of squares of elements in the list given as parameter"
    s=0
    for x in lst:
        s += x**2
    return s
#call function and pass values into it
print(sum_of_squares(3, 4))

lst=[1,5,8]
print("With list unpacked as arguments to the functions:", sum_of_squares(*lst))
# print(sum_of_squares(lst))    # Does not work correctly

def f():            # outer function
    b=2
    def g():        # inner function
        # nonlocal b # Without this nonlocal statement,
        b=3         # this will create a new local variable
        print(b)
    g()
    print(b)
f()

def TowerOfHanoi(n , source, destination, auxilliary): 
    if n==1: 
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxilliary, destination) 
    print("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxilliary, destination, source)