#
# Created on Tue May 24 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
class Solution:
    def bubbleSort(self, input_array):
        #When we are given an array of N elements and we are not allowed to swap the non-consecutive indices
        #then we will keep swapping the consecutive elements only if A[i] > A[i+1] 
        #that leads to moving the bigger element at its last position in each iteration
        #i.e., bubbling up the larger bubble at its last position -- Bubble sort

        size = len(input_array)
        for i in range(size):
            for j in range(i+1, size):
                if input_array[i] > input_array[j]:
                   #swap
                   input_array[i], input_array[j] = input_array[j], input_array[i]
        
        return input_array
        #Time: O(N**2)
    
s = Solution()
A = [9,3,8,6,7,2,11,4,5]
ans = s.bubbleSort(A)
#print(ans)
assert ans == [2, 3, 4, 5, 6, 7, 8, 9, 11]
                    
