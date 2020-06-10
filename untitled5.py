# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:41:58 2020

@author: noble
"""


my_attrbs = {'height':1.84,'weight':81.6,'fav color':'green'}

while True:
    q = input("What would you like to know: Height, Weight, or fav color: ")
    q = q.lower()
    if q in my_attrbs:
        print(my_attrbs[q])
        break
    else:
        print("Not valid input, try again")