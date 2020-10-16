# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:51:02 2020

@author: Bhagyashree
"""

#function definition
def most_frequent():
    print("please enter the string")
most_frequent()

frequencies = {} 
  
for char in "Mississippi": 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

# Show Output
print ("Per char frequency in '{}' is :\n {}".format("Mississippi", str(frequencies)))
