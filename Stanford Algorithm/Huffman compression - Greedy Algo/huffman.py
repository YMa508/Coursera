# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 09:49:25 2019

@author: YM4558
"""

file = open("huffman.txt", "r")
#file = open("test.txt", "r") 
data = file.read().splitlines() # use splitlines() to remove the newlines
num = int(data[0])
vals = [int(val) for val in data[1:]] # then convert from string to integer

import heapq

class HeapNode(object):
    
    def __init__(self, freq, char):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None
    
    # tell the heapq use which attribute to sort
    def __lt__(self, other):
        return self.freq < other.freq

myheap = []
for char in range(num):
    node = HeapNode(vals[char], char)
    heapq.heappush(myheap, node)
    
def compress(heap):
    if len(heap) == 2:
        merge = HeapNode(heap[0].freq + heap[1].freq, None)
        merge.left = heap[0]
        merge.right = heap[1]
        return merge
    elif len(heap) > 2:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merge = HeapNode(node1.freq + node2.freq, None)
        merge.left = node1
        merge.right = node2
        heapq.heappush(heap, merge)
        return compress(heap)
        
a = compress(myheap)

def MinLen(comp):
    if comp.char is not None:
        return 0
    elif (comp.left.char is not None) or (comp.right.char is not None):
        return 1
    else:
        return min(MinLen(comp.left), MinLen(comp.right)) + 1
    
def MaxLen(comp):
    if comp.char is not None:
        return 0
    elif (comp.left.char is not None) and (comp.right.char is not None):
        return 1
    else:
        return max(MaxLen(comp.left), MaxLen(comp.right)) + 1
    
print(MinLen(a), MaxLen(a)) # 9, 19