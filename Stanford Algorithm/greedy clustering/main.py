# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:11:09 2019

@author: YM4558
"""

import UnionFind
import numpy as np
import pandas as pd
import math
import time

start_time = time.time()
text_file = open("clustering1.txt", "r")
lines = text_file.read().splitlines()
num = int(lines[0])

arr = np.zeros((len(lines) - 1, 3))
for i, line in enumerate(lines[1:]):
    arr[i, :] = line.split()
    
df = pd.DataFrame(arr, columns = np.array(['edge1', 'edge2', 'cost']))
sortdf = df.sort_values(['cost'], axis = 0, ascending = True)
sortdf = sortdf.applymap(int)
sortarr = sortdf.values
print("load and sort--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
test = UnionFind.UF(num)
count = 0
k = 4
space = math.inf
for row in sortarr:
    i, j = row[0], row[1]
    if count < num - k:
        if not test.connected(i - 1, j - 1):
            test.union(i - 1, j - 1)
            count += 1
    else:
        if not test.connected(i - 1, j - 1):
            space = min(space, row[2])
print("maximum spacing:", space) # 106
print("--- %s seconds ---" % (time.time() - start_time))
#https://www.coursera.org/learn/algorithms-greedy/discussions/weeks/2/threads/mSGCyQULEemZUwrw3z8SgA