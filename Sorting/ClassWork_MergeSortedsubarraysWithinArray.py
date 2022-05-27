#
# Created on Fri May 27 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given an array of size N and 3 indexes  l, y, r where A[l:y-1] and A[y:r] are sorted and they're contiguous
Now, sort A[l:r] by merging above two independently sorted subarrays
'''
class Solution:
    def merge(self, input_array, start1, start2, end2):
        end1 = start2 -1
        #start2-1 will be end1, as they're contiguous
        #Here the arrays [start1: start2-1] and [start2:end2] are independently sorted
        #now we've to merge them into a sorted one

        #lets create a temporary array to store the merged sorted array
        temp_result = [] #its size will be "end2 - start1 + 1"
        
        #lets have two pointers pointing array1 and array2.
        p1 = start1
        p2 = start2

        while p1 <= end1 and p2 <= end2:
            if input_array[p1] < input_array[p2]:
                temp_result.append(input_array[p1])
                p1 += 1
            elif input_array[p1] > input_array[p2]:
                temp_result.append(input_array[p2])
                p2 += 1
            else:
                temp_result.append(input_array[p1])
                temp_result.append(input_array[p2])
                p1 += 1
                p2 += 1
        
        if p1 > end1:
            for ele in input_array[p2:end2+1]:
                temp_result.append(ele)
        elif p2 > end2:
            for ele in input_array[p1:end1+1]:
                temp_result.append(ele)
        
        i = 0
        for ptr in range(start1, end2+1):
            input_array[ptr] = temp_result[i]
            i += 1
        
        return input_array
    
    def mergeSort(self, input_array, leftPtr, rightPtr):
        if leftPtr == rightPtr:
            return
        
        midPtr = (leftPtr + rightPtr)//2

        self.mergeSort(input_array, leftPtr, midPtr)
        self.mergeSort(input_array, midPtr+1, rightPtr)
        
        self.merge(input_array, leftPtr, midPtr+1, rightPtr)
        return input_array

s = Solution()
#arr = [8, 1, 3, 6, 11, 2, 4, 9, 7, 6]
#ans = s.merge(arr, start1=2, start2=5, end2=7)
#print(ans)
arr = [8, 1, 3, 6, 11, 2, 4, 9, 7, 6]
sorted_arr = s.mergeSort(arr[:], 0, len(arr)-1)
x = sorted(arr)
assert sorted_arr == x
print(arr)
print(x)
print(sorted_arr)    

