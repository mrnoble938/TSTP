# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:27:32 2020

@author: noble

Fizzbuzz example:
Write a program that prints the numbers from 1 to 100. But for multiples 
of three print "Fizz" instead of the number and for the multiples of five 
prin "Buzz". For numbers which are multiples of both three and 
five print "FizzBuzz".
"""


def fizzbuzz():
    for i in range(1,101):
        fizz = (i % 3 == 0)
        buzz = (i % 5 == 0)
        if fizz and buzz:
            print("FizzBuzz")
        elif fizz:
            print("Fizz")
        elif buzz:
            print("Buzz")
        else:
            print(i)
            
fizzbuzz()

