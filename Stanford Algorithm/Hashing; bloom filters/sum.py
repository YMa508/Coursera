# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:25:12 2019

@author: YM4558
"""
import time

file = open("prob-2sum.txt", "r")
#file = open("case1.txt", "r") 
data = file.read().splitlines() # use splitlines() to remove the newlines
vals = [int(val) for val in data] 

# insert elements into hash table (dict)
start_time = time.time()
targets = list(range(-10000, 10001))
#targets = [3, 10]
count = 0
d = {}
#sums = []
remove_l = []
for x in vals:
    for tgt in list(set(targets) - set(remove_l)):
        #print(x, tgt)
        if (tgt - x) in d and (tgt - x) != x:# and (tgt - x) != x:
            #targets.remove(tgt)

            remove_l.append(tgt)
            count += 1
            #sums.append(tgt)
    d[x] = x
print(count)
print("--- %s seconds ---" % (time.time() - start_time))