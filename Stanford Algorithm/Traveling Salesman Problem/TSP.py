# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:27:18 2019

@author: YM4558
"""
import time
from itertools import combinations
import numpy as np
import math

start_time = time.time()

# Seperate the problem to 0 - 12 and 11 - 25
# Then the answer is the sum of these two minus 
# twice of the disctance between 11 and 12

#text_file = open("input_float_76_20.txt", "r")
text_file = open("tsp1.txt", "r")
lines = text_file.read().splitlines()

num = int(lines[0])

cord = np.zeros((num, 2))

for idx, line in enumerate(lines[1:]):
    x, y = line.split()
    cord[idx, :] = [float(x), float(y)]

dist = np.zeros((num, num))
for i in range(num):
    for j in range(num):
        #if i != j:
        dist[i, j] = sum((cord[i, :] - cord[j, :])**2)**0.5

print("pre-processing:--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
# prepare the combination list
elements = list(range(1, num))
# starting from 1 instead of 0 as the first element always need be included
comb = []
for i in range(1, num):
    comb += list(combinations(elements, i))
comb = [tuple()] + comb

A = np.ones((2**(num - 1), num)) * math.inf
A[0, 0] = 0

for i, c in enumerate(comb):
    for j in c:
        #print(c, j)
        reduced_S = tuple(sorted(set(c) - set([j])))
        i_prime = comb.index(reduced_S)
        A[i, j] = min(A[i_prime, :] + dist[:, j])
        
res1 = min(A[-1, :] + dist[:, 0])
print(res1)
print("execution:--- %s seconds ---" % (time.time() - start_time))

d = dist[11, 12]

start_time = time.time()

#text_file = open("input_float_76_20.txt", "r")
text_file = open("tsp2.txt", "r")
lines = text_file.read().splitlines()

num = int(lines[0])

cord = np.zeros((num, 2))

for idx, line in enumerate(lines[1:]):
    x, y = line.split()
    cord[idx, :] = [float(x), float(y)]

dist = np.zeros((num, num))
for i in range(num):
    for j in range(num):
        #if i != j:
        dist[i, j] = sum((cord[i, :] - cord[j, :])**2)**0.5

print("pre-processing:--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
# prepare the combination list
elements = list(range(1, num))
# starting from 1 instead of 0 as the first element always need be included
comb = []
for i in range(1, num):
    comb += list(combinations(elements, i))
comb = [tuple()] + comb

A = np.ones((2**(num - 1), num)) * math.inf
A[0, 0] = 0

for i, c in enumerate(comb):
    for j in c:
        #print(c, j)
        reduced_S = tuple(sorted(set(c) - set([j])))
        i_prime = comb.index(reduced_S)
        A[i, j] = min(A[i_prime, :] + dist[:, j])
        
res2 = min(A[-1, :] + dist[:, 0])
print(res2)
print("execution:--- %s seconds ---" % (time.time() - start_time))

final = res1 + res2 - 2 * d
print(final) # 26442.730308954753