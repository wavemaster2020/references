# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

for i in range(0,10, 1):
    print(i)

i = 0
print()

while (i<10): 
    print(i)
    i = i + 1

# define the function blocks
def zero():
    print ("You typed zero.\n")

def sqr():
    print ("n is a perfect square\n")

def even():
    print ("n is an even number\n")

def prime():
    print ("n is a prime number\n")

    
# Equivalent to a case/switch statement    
# map the inputs to the function blocks
options = {0 : zero,
           1 : sqr,
           4 : sqr,
           9 : sqr,
           2 : even,
           3 : prime,
           5 : prime,
           7 : prime,
}

options[5]()
# math operators: + - * / % ** (power) // (divide and floor)

5**2

5%2

5/2

import numpy as py
py.sqrt(8)

'{:10}'.format('test')

squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


class Foo:
    def __init__(self, val):
        self.val = val
    def printVal(self):
        print(self.val)

# This is a test for a class

obj1 = Foo(1)

obj1.printVal()

# This is a test for a for loop

for i in range (1, 10):
    print(i); 
    print(i);
    
   

