# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:16:50 2019

@author: YM4558
"""

class UF(object):
    
    def __init__(self, num):
        self.leaders = [i for i in range(num)]
        
    def find(self, idx):
        leader = self.leaders[idx]
        if idx != leader:
            leader = self.find(leader)
        return leader
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.leaders[pi] = pj
    
    def connected(self, i, j):
        return self.find(i) == self.find(j)
    
if __name__ == "__main__":
    test = UF(10)
    connections = [(0, 1), (1, 2), (0, 9), (5, 6), (6, 4), (5, 9)]
    for i, j in connections:
        test.union(i, j)
        
    for i in range(10):
        print('item', i, '-> component', test.find(i))
        
    print(test.connected(2, 5))
    print(test.connected(3, 5))