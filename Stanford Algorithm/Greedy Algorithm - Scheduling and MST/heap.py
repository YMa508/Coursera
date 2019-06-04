# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:37:46 2019

@author: YM4558
"""
import math

class Heap(object):
    
    def __init__(self):
        self.heap = []
        # for house keeping purpose
        self.Xns = []
        self.nodes = []
    
    def parent(self, idx):
        return int(math.floor(idx/2))
    
    def insert(self, Xn, node, key):
        self.Xns.append(Xn)
        self.nodes.append(node)
        self.heap.append(key)
        #if parent of key is samller the key, it's done
        if len(self.heap) > 1:
            idx = len(self.heap)
            parent_idx = self.parent(idx)
            # need check whether the idx is already the root, if so stop the bubble up
            while (self.heap[parent_idx - 1] > self.heap[idx - 1]) and (idx > 1):
                self.heap[parent_idx - 1], self.heap[idx - 1] = self.heap[idx - 1], self.heap[parent_idx - 1]
                self.nodes[parent_idx - 1], self.nodes[idx - 1] = self.nodes[idx - 1], self.nodes[parent_idx - 1]
                self.Xns[parent_idx - 1], self.Xns[idx - 1] = self.Xns[idx - 1], self.Xns[parent_idx - 1]
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
            self.nodes[i - 1], self.nodes[smallest - 1] = self.nodes[smallest - 1], self.nodes[i - 1]
            self.Xns[i - 1], self.Xns[smallest - 1] = self.Xns[smallest - 1], self.Xns[i - 1]
            self.MinHeapify(smallest)

    
    def extractMin(self):
        # swap the last element and the root
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.nodes[0], self.nodes[-1] = self.nodes[-1], self.nodes[0]
        self.Xns[0], self.Xns[-1] = self.Xns[-1], self.Xns[0]
        # remove the last element which is the original root
        Min = self.heap.pop()
        Minnode = self.nodes.pop()
        MinXn = self.Xns.pop()
        self.MinHeapify(1)
        return Min, MinXn, Minnode
    
    def bubbleup(self, idx):
        if len(self.heap) > 1:
            parent_idx = self.parent(idx)
            #print(len(self.nodes), len(self.heap), parent_idx, idx)
            while (self.heap[parent_idx - 1] > self.heap[idx - 1]) and (idx > 1):
                self.heap[parent_idx - 1], self.heap[idx - 1] = self.heap[idx - 1], self.heap[parent_idx - 1]
                self.nodes[parent_idx - 1], self.nodes[idx - 1] = self.nodes[idx - 1], self.nodes[parent_idx - 1]
                self.Xns[parent_idx - 1], self.Xns[idx - 1] = self.Xns[idx - 1], self.Xns[parent_idx - 1]
                #self.bubbleup(parent_idx)
    
    def delNode(self, i):
        self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
        self.nodes[i], self.nodes[-1] = self.nodes[-1], self.nodes[i]
        self.Xns[i], self.Xns[-1] = self.Xns[-1], self.Xns[i]
        self.heap.pop()
        self.nodes.pop()
        self.Xns.pop()
        if i < len(self.heap): # avoid the case where last node is deleted
            self.bubbleup(i + 1)
            self.MinHeapify(i + 1)
    
    def display(self):
        print(self.heap)
    
if __name__ == "__main__":
    pass
#    h = Heap()
#    h.insert(4, 1, 3)
#    h.insert(2, 3, 4)
#    h.insert(7, 9, 8)
#    h.insert(-5, 9, 98)
#    h.display()
#    h.delNode(2)  
#    h.display()
#    h.extractMin()
#    h.display()
#    # heap elements
    #heap_list = [4, 4, 8, 9, 4, 12, 9, 11, 13]
#    # initialize heap as array
#    h = Heap()
#    for idx, item in enumerate(heap_list):
#        h.insert(idx, item)
#    h.display()
#    a = h.extractMin()
#    h.display()
#    h.delNode(1)
#    h.display()
#    a = h.extractMin()
#    h.display()
#    a = h.extractMin()
#    h.display()

#for i, x in enumerate(heap_list):
#    print(i, x)