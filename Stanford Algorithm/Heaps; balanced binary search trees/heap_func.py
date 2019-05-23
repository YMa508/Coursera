# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:57:46 2019

@author: YM4558
"""

import math

# Array implementation of Heap

# Parent method for Heap
def parent(idx): # note idx should not be 1 as it has no parent
    return math.floor(idx/2)

# Insert method for Heap
def insert(heap, key):
    heap.append(key)
    #if parent of key is samller the key, it's done
    if len(heap) > 1:
        idx = len(heap)
        parent_idx = parent(idx)
        while heap[parent_idx - 1] > heap[idx - 1]:
            heap[parent_idx - 1], heap[idx - 1] = heap[idx - 1], heap[parent_idx - 1]
            idx = parent_idx
            parent_idx = parent(idx)

# when we use the index to slice the array, don't forget -1
def MinHeapify(heap, i):
    l = 2 * i
    r = 2 * i + 1
    if l <= len(heap) and heap[l - 1] < heap[i - 1]:
        smallest = l
    else:
        smallest = i
    if r <= len(heap) and heap[r - 1] < heap[smallest - 1]:
        smallest = r
    if smallest != i:
        heap[i - 1], heap[smallest - 1] = heap[smallest - 1], heap[i - 1]
        MinHeapify(heap, smallest)


def extractMin(heap):
    # swap the last element and the root
    heap[0], heap[-1] = heap[-1], heap[0]
    # remove the last element which is the original root
    Min = heap.pop()
    MinHeapify(heap, 1)
    return Min

if __name__ == "__main__":
    # heap elements
    heap_list = [4, 4, 8, 9, 4, 12, 9, 11, 13]
    # initialize heap as array
    heap = []
    for item in heap_list:
        insert(heap, item)
    print(heap)
    extractMin(heap)
    print(heap)
    extractMin(heap)
    print(heap)
    extractMin(heap)
    print(heap)