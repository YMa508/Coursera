# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 10:03:47 2019

@author: ym4558
"""
import numpy as np
def ChoosePivot(A, l, r):
    return A[l]
#    first = A[l]
#    last = A[r]
#    if (r - l)%2 == 0:
#        middle = A[int(l+(r-l)/2)]
#    else:
#        middle = A[int(l + (r-l-1)/2)]
#    return np.median([first, last, middle])

def Partition(A, l, r):
    # 
    p = A[l] 
    i = l + 1
    for j  in range(l + 1, r + 1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
    # swap the pivot with the last element smaller than pivot
    A[l], A[i - 1] = A[i - 1], A[l]
    return i



def QuickSort(my_list, l, r):
    if l == r:
        return 0
    else:
        p = ChoosePivot(my_list, l, r)
        #print('pivot', p)
        count = 0
        #print(my_list, p)
        # swap the pivot withe the first element
        p_idx = my_list.index(p)
        if p_idx != l:
            my_list[l], my_list[p_idx] = my_list[p_idx], my_list[l]
        # Partition around p
        idx = Partition(my_list, l, r)
        count = r - l
        #count += idx - 2 - l + r - idx
        #print('idx', idx)
        # Recursive calls Quicksort to left and right part
        #x = y = 0
        if idx > l + 1:# if idx = 0, no need for Quicksort on 1st part
            #QuickSort(my_list[l:idx - 1], l, idx - 2)
            x = QuickSort(my_list, l, idx - 2)
            #count += idx - 2 - l + 1
        else:
            x = 0
        if idx < r + 1:
            #print(my_list[idx:r + 1], idx, r)
            #QuickSort(my_list[idx:r + 1], idx, r)
            y = QuickSort(my_list, idx, r)
            #count += r - idx + 1
        else:
            y = 0
        #print('count', count)
    return x + y + count
#test1 = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
#test1 = [20, 19]#, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
#test1 = [2, 1, 3]
#print(QuickSort(test1, 0, len(test1) - 1))
#print(test1)

text_file = open("QuickSort.txt", "r")
lines = text_file.read().splitlines()
lines = list(map(int, lines))
#lines = lines[5:10]
#print(lines)
print(QuickSort(lines, 0, len(lines) - 1))

#left: 162085
#right:164123
#middle:138382