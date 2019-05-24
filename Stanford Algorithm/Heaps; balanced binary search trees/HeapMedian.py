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

# initialize max_heap and min_heap
MaxHeap = heap.Heap() # to store the lower half
MinHeap = heap.Heap() # to store the upper half

Medians = []

for val in vals:
    if not MaxHeap.heap:
        MaxHeap.insert(-val)
        Medians.append(val)
    else:
        if val >= -MaxHeap.heap[0]:
            MinHeap.insert(val)
        else:
            MaxHeap.insert(-val)
        
        if len(MaxHeap.heap) == len(MinHeap.heap):
            Medians.append(-MaxHeap.heap[0])
        elif len(MaxHeap.heap) == len(MinHeap.heap) + 1:
            Medians.append(-MaxHeap.heap[0])
        elif len(MinHeap.heap) == len(MaxHeap.heap) + 1:
            Medians.append(MinHeap.heap[0])
            # handle the case when the rebalancing is required
        elif len(MaxHeap.heap) == len(MinHeap.heap) + 2:
            MinHeap.insert(-MaxHeap.extractMin())
            Medians.append(-MaxHeap.heap[0])
        elif len(MinHeap.heap) == len(MaxHeap.heap) + 2:
            MaxHeap.insert(-MinHeap.extractMin())
            Medians.append(-MaxHeap.heap[0])
    
    #print(val, MaxHeap.heap, MinHeap.heap)
print(sum(Medians)%10000)