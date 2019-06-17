# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:36:15 2019

@author: YM4558
"""
import numpy as np
import time

text_file = open("knapsack1.txt", "r")
lines = text_file.read().splitlines()
knapsacksize, num = lines[0].split()
knapsacksize = int(knapsacksize)
num = int(num)

start_time = time.time()

vals = []
weights = []

for line in lines[1:]:
    v, w = line.split()
    vals.append(int(v))
    weights.append(int(w))

A = np.zeros((num + 1, knapsacksize + 1))
for i in range(1, num + 1):
    for x in range(knapsacksize + 1):
        if weights[i - 1] > x:
            A[i, x] = A[i - 1, x]
        else:
            # must include the above edge case, otherwise x - wi is negative, 
            # it's go to the wrong place in the array
            A[i, x] = max(A[i - 1, x],  A[i - 1, x - weights[i - 1]] + vals[i - 1])

print(A[-1, -1]) # 2493893
print("--- %s seconds ---" % (time.time() - start_time))