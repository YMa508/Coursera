# -*- coding: utf-8 -*-
"""
Created on Fri May 31 09:58:06 2019

@author: YM4558
"""
import numpy as np
import pandas as pd

text_file = open("jobs.txt", "r")
lines = text_file.read().splitlines()
num = lines[0]
#weights = []
#lengths = []
#for line in lines[1:]:
#    w, l = line.split()
#    weights.append(int(w))
#    lengths.append(int(l))

def diff(line):
    w, l = line.split()
    # return a tuple such that the second will handle when tie breaks
    return int(w) - int(l), int(w) 

def ratio(line):
    w, l = line.split()
    return int(w)/int(l)

def schedule(lines, key):
    # sort the lines based on the key (the key could be set using lambda function)
    sortlines = sorted(lines[1:], key = key, reverse = True)
    weights = []
    lengths = []
    for line in sortlines:
        w, l = line.split()
        weights.append(int(w))
        lengths.append(int(l))
    times = np.cumsum(lengths)

    a = times*weights
    # need use float 64 as the correct sum is already larger than 
    # the maximum number supported by float32
    return np.sum(a, dtype = np.float64)

if __name__ == "__main__":
    print(schedule(lines, diff)) #69119377652
    print(schedule(lines, ratio)) # 67311454237 