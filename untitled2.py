# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:39:57 2020

@author: noble
"""
def even_odd():
    '''
    Returns whether user defined value is even or odd
    -------
    user input n must be a number

    '''
    n = input("Enter a number:")
    n = int(n)
    if n % 2 == 0:
        print("Even\n")
    else:
        print("Odd\n")
        
        
even_odd()
even_odd()
even_odd()

# optional parameters get defined with default value in the function definition
def add_it(x,y=10):
    return x + y

result = add_it(2,7)
print(result,"\n")

# try/except is for exception handling
try:
    a = input("type a num:")
    b = input("type a num:")
    a = int(a)
    b = int(b)
    print (a/b)
except (ZeroDivisionError,ValueError):
    print("Invalid INput")


