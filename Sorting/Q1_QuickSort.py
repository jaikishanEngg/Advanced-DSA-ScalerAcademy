#
# Created on Thu Jun 02 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an integer array A, sort the array using QuickSort.

Problem Constraints
1 <= |A| <= 105
1 <= A[i] <= 109

Input Format
    First argument is an integer array A.

Output Format
    Return the sorted array.

Example Input
Input 1:
     A = [1, 4, 10, 2, 1, 5]

Input 2:
    A = [3, 7, 1]

Example Output
Output 1:
    [1, 1, 2, 4, 5, 10]

Output 2:
    [1, 3, 7]

Example Explanation
Explanation 1:
    Return the sorted array.
'''
import random

class Solution:
    def randomized_quicksort(self, input_array, start, end):
        random_index = random.randint(start, end)
        #swap the elements at index 0, random_index of input_array
        input_array[0], input_array[random_index] = input_array[random_index], input_array[0]
        
        pivot_index = self.partition(input_array, start, end)
        self.quicksort(input_array, start, pivot_index - 1)
        self.quicksort(input_array, pivot_index + 1, end)
        
        return input_array

    def partition(self, input_array, start, end):
        #Here the pivot element would be input_array[start]
        pivot = input_array[start]

        left_ptr = start + 1
        right_ptr = end

        while left_ptr <= right_ptr:
            if input_array[left_ptr] <= pivot:
                left_ptr += 1
            
            elif input_array[right_ptr] >= pivot:
                right_ptr -= 1
            
            else:
                #swap elements at left and right pointers
                input_array[left_ptr], input_array[right_ptr] = input_array[right_ptr], input_array[left_ptr]
                left_ptr += 1
                right_ptr -= 1
        
        #swap pivot, right_ptr element
        input_array[right_ptr], input_array[start] = input_array[start], input_array[right_ptr]
        return right_ptr

    def quicksort(self, input_array, start, end):
        if start > end:
            return

        pivot_index = self.partition(input_array, start, end)
        self.quicksort(input_array, start, pivot_index - 1)
        self.quicksort(input_array, pivot_index+1, end)
        return input_array

    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        #return self.quicksort(A, 0, len(A) - 1)
        return self.randomized_quicksort(A, 0, len(A) - 1)

s = Solution()
input_array = [1, 3, 7, 4, 0, 2]
print(s.solve(input_array))

