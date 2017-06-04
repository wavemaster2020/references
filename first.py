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

5**2

5%2

5/2

import numpy as py
py.sqrt(8)

'{:10}'.format('test')

# lists

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.index('apple'))
fruits.sort()
fruits.pop()
fruits.append(3.14)
print(fruits.index('apple'))

for i in fruits:
    print(i)

squares = [x**2 for x in range(10)]

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

