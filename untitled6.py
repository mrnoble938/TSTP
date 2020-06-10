# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:18:23 2020

@author: noble
"""


in1 = input("Enter a noun: ")
in2 = input("Enter another noun: ")

sentence = "Yesterday I wrote a {}.  I sent it to {}!".format(in1,in2)
print(sentence)

lst = ["The",
       "fox",
       "jumped",
       "over",
       "the",
       "fence",
       "."
       ]

ones = " ".join(lst[:-1]) + lst[-1]pe
print(ones)