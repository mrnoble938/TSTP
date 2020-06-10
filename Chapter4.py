# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:08:15 2020

@author: noble

Chapter 4 Challenges
"""

# def square():
#     try:
#         x = input("enter a number:")
#         x = int(x)
#         result = x ** 2
#         print(result)
#     except ValueError:
#         print("Must be a number")

# square()

# def printstring():
#     x = input("Enter a string:")
#     print(x)
    
# printstring()

# def bigfunc(x,y,z,a=1,b=1):
#     '''
#     Parameters
#     ----------
#     x : integer or float
#     y : integer or float
#     z : integer or float
#     a : integer or float, optional
#         Power on x. The default is 1.
#     b : integer or float, optional
#         Power on y. The default is 1.

#     Returns x^a + y^b + z
#     -------

#     '''
#     result = x ** a + y ** b + z
#     return result

# result = bigfunc(2,2,2,3,3)
# print(result)

def div_two(x):
    a = x / 2
    return a

def mult_four(x):
    a = x * 4
    return a

b = div_two(10)
c = mult_four(b)
print(c)

def string2float():
    try:
        x = input("Enter a number:")
        x = float(x)
        print(x)
    except ValueError:
        print("Invalid input")
        
string2float()
    