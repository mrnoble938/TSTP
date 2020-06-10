# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:13:58 2020

@author: noble
"""


def removeDuplicates(nums):
    count = 0    
    while count < len(nums):
            print(nums)
            print('count = {}'.format(count))
            print('val = {}'.format(nums[count]))
            if (count > 0) and nums[count] == nums[count - 1]:
                nums.pop(count)
                count = count
            else:
                count += 1    
    return len(nums)