# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:14:20 2020

@author: noble
"""

nums = [2, 5, 45, 8, 90, 85, 44, 32, 67, 12, 3, 2, 7, 10, 21, 59]

while True:
    n = input('Guess a number (or press q to quit): ')
    if n == 'q':
        break
    else:
        if int(n) in nums:
            print('You guessed right')
        else:
            print('Nope')