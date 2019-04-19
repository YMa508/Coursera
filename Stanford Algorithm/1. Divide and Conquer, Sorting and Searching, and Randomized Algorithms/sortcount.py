# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:53:49 2019

@author: ym4558
"""

def sortCount(my_list):
    #count = 0
    if len(my_list) > 1:
        mid = int(len(my_list)/2)
        L = my_list[:mid]
        R = my_list[mid:]

        x = sortCount(L)
        y = sortCount(R)
        
        ############## 
        # Count Split Inversion
        #############
        
        #sorted_list = []
        # Initiate i, j and k
        count = 0
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                my_list[k] = L[i]
                i += 1
            else:
                my_list[k] = R[j]
                j += 1
                count += len(L) - i
                #print(L, R)
                #print(len(L) - i)
            k += 1
        
        while i < len(L):
            my_list[k] = L[i]
            i += 1
            k += 1
                
        while j < len(R):
            my_list[k] = R[j]
            j += 1
            k += 1
        
        return x + y + count
    else:
        #return my_list
        #count = 0
        return 0
    #print(x)
    #return x + y + count
    
test1 = [13, 5, 63, 7, 101, 12, 36]
test2 = [13, 14, 8, 71, 7, 9]
test = [9, 2, 13, 1]
#print(sortCount(test))
#print(test)

text_file = open("IntegerArray.txt", "r")
lines = text_file.read().splitlines()
lines = list(map(int, lines))
print(sortCount(lines))