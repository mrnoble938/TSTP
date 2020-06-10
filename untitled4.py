# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:08:05 2020

@author: noble
"""


colors = ["purple",
          "orange",
          "green"]

while True:
    guess = input('Guess a color:')
    if guess in colors:
        print("You guessed right!")
        break
    else:
        print("Wrong, try again")
    