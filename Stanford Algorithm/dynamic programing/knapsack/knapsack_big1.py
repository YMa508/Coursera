import numpy as np
import time

#text_file = open("knapsack1.txt", "r")
text_file = open("knapsack_big.txt", "r")
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

A = np.zeros((2, knapsacksize + 1))
for i in range(1, num + 1):
    #for x in range(weights[i - 1], knapsacksize + 1):
    A[1, weights[i - 1]:] = np.maximum(A[0, weights[i - 1]:],  A[0, 0:(knapsacksize + 1 - weights[i - 1]) ] + vals[i - 1])
    A[0, :] = A[1, :]

print(A[1, -1]) #4243395
print("--- %s seconds ---" % (time.time() - start_time))