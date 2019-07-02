# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:08:37 2019

@author: YM4558
"""

import time
import numpy as np
import math

start_time = time.time()

text_file = open("nn.txt", "r")
lines = text_file.read().splitlines()

num = int(lines[0])

cord = np.zeros((num, 2))
#cord_x = []
#cord_y = []

for idx, line in enumerate(lines[1:]):
    i, x, y = line.split()
    cord[idx, :] = [float(x), float(y)]

tours = [1]
lastc = 1
totaldist = 0
while len(tours) < num:
#    if len(tours)%100 == 0:
#        print(len(tours))
    min_dist = math.inf
    min_city = 0
    # search upward
    for city in range(lastc + 1, num + 1):
        if city not in tours:
            if abs((cord[lastc - 1, :] - cord[city - 1, :])[0]) > min_dist:
                break
            dist = sum((cord[lastc - 1, :] - cord[city - 1, :])**2)**0.5
#            if lastc == 11:
#                print(lastc, city, dist, min_dist)
            tie = min_dist == dist
            min_dist = min(min_dist, dist)
            # cannot only use min_dist == dist (to solve the tiebreak)
            if (min_dist == dist) & (not tie): 
                min_city = city
    # search downward
    for city in reversed(range(2, lastc)):
        if city not in tours:
            if abs((cord[lastc - 1, :] - cord[city - 1, :])[0]) > min_dist:
                break

            dist = sum((cord[lastc - 1, :] - cord[city - 1, :])**2)**0.5
#            if lastc == 11:
#                print(lastc, city, dist, min_dist)
            tie = min_dist == dist
            min_dist = min(min_dist, dist)
            if min_dist == dist: 
                min_city = city
    
    tours.append(min_city)
    totaldist += min_dist
    lastc = min_city
    
#print(tours)
last_hop = sum((cord[lastc - 1, :] - cord[0, :])**2)**0.5
print(totaldist + last_hop) #1203406

print(":--- %s seconds ---" % (time.time() - start_time))