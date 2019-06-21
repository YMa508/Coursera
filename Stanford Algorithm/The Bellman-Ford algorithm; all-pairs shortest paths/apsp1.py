# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:15:14 2019

@author: YM4558
"""
import numpy as np
#import itertools
import math
import time

text_file = open("test.txt", "r")
lines = text_file.read().splitlines()
num_nodes = int(lines[0].split()[0])
num_edges = int(lines[0].split()[1])

#edges = []
#costs = []
d = {}

for line in lines[1:]:
    n1, n2, c = line.split()
    d[(int(n1), int(n2))] = int(c)
#    edges.append((int(n1), int(n2)))
#    costs.append(int(c))
    
# initiate the 3D A-Matrix
A = np.zeros((num_nodes, num_nodes, 2))
for i in range(num_nodes):
    for j in range(num_nodes):
        if (i + 1, j + 1) in d:
            A[i, j, 0] = d[(i + 1, j + 1)]
        elif i != j:
            A[i, j, 0] = math.inf
        
start_time = time.time()
for k in range(num_nodes):
    for i in range(num_nodes):
        for j in range(num_nodes):
            A[i, j, 1] = np.minimum(A[i, j, 0], A[i, k, 0] + A[k, j, 0])
    A[:, :, 0] = A[:, :, 1]
    
print("--- %s seconds ---" % (time.time() - start_time))

if np.amin(np.diagonal(A[:,:,1])) < 0:
    print(None)
else:
    print(np.amin(A[:,:,1]))