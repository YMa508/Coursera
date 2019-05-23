# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:57:46 2019

@author: YM4558
"""

import math
import heap

file = open("Median.txt", "r") 
data = file.read().splitlines() # use splitlines() to remove the newlines
vals = [int(val) for val in data] # then convert from string to integer