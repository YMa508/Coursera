# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:53:49 2019

@author: ym4558
"""

def mergeSort(my_list):
    if len(my_list) > 1:
        mid = int(len(my_list)/2)
        L = my_list[:mid]
        R = my_list[mid:]

        sorted_L = mergeSort(L)
        sorted_R = mergeSort(R)
        
        ############## 
        # Merge Steps
        #############
        
        sorted_list = []
        # Initiate i, j and k
        i = j = 0
        while i < len(sorted_L) and j < len(sorted_R):
            if sorted_L[i] < sorted_R[j]:
                sorted_list.append(sorted_L[i])
                i += 1
            else:
                sorted_list.append(sorted_R[j])
                j += 1
        
        while i < len(sorted_L):
            sorted_list.append(sorted_L[i])
            i += 1
                
        while j < len(sorted_R):
            sorted_list.append(sorted_R[j])
            j += 1
        return sorted_list
    else:
        return my_list
    
test1 = [13, 5, 63, 7, 101, 12, 36]
test2 = [13, 14, 8, 71, 7, 9]
#print(mergeSort(test2))

text_file = open("IntegerArray.txt", "r")
lines = text_file.read().splitlines()
lines = list(map(int, lines))
mergeSort(lines)