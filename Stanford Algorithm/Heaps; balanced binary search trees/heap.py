# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:37:46 2019

@author: YM4558
"""
import math

class Heap(object):
    
    def __init__(self):
        self.heap = []
    
    def parent(self, idx):
        return math.floor(idx/2)
    
    def insert(self, key):
        self.heap.append(key)
        #if parent of key is samller the key, it's done
        if len(self.heap) > 1:
            idx = len(self.heap)
            parent_idx = self.parent(idx)
            while self.heap[parent_idx - 1] > self.heap[idx - 1]:
                self.heap[parent_idx - 1], self.heap[idx - 1] = self.heap[idx - 1], self.heap[parent_idx - 1]
                idx = parent_idx
                parent_idx = self.parent(idx)
    
    def MinHeapify(self, i):
        l = 2 * i
        r = 2 * i + 1
        if l <= len(self.heap) and self.heap[l - 1] < self.heap[i - 1]:
            smallest = l
        else:
            smallest = i
        if r <= len(self.heap) and self.heap[r - 1] < self.heap[smallest - 1]:
            smallest = r
        if smallest != i:
            self.heap[i - 1], self.heap[smallest - 1] = self.heap[smallest - 1], self.heap[i - 1]
            self.MinHeapify(smallest)

    
    def extractMin(self):
        # swap the last element and the root
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        # remove the last element which is the original root
        Min = self.heap.pop()
        self.MinHeapify(1)
        return Min
    
    def display(self):
        print(self.heap)
    
if __name__ == "__main__":
    # heap elements
    heap_list = [4, 4, 8, 9, 4, 12, 9, 11, 13]
    # initialize heap as array
    h = Heap()
    for item in heap_list:
        h.insert(item)
    h.display()
    a = h.extractMin()
    h.display()
    a = h.extractMin()
    h.display()
    a = h.extractMin()
    h.display()