#
# Created on Thu Jun 02 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a sorted array A of size N and a target value B, return the index (0-based indexing) if the target is found.
If not, return the index where it would be if it were inserted in order.

NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.

Problem Constraints
1 <= N <= 106

Input Format
    The first argument is an integer array A of size N.
    The second argument is an integer B.

Output Format
    Return an integer denoting the index of target value.

Example Input
Input 1:
    A = [1, 3, 5, 6]
    B = 5 

Input 2:
    A = [1]
    B = 1

Example Output
Output 1:
    2 

Output 2:
    0

Example Explanation
Explanation 1:
    The target value is present at index 2. 

Explanation 2:
    The target value is present at index 0.
'''
class Solution:
    def binarysearch(self, input_array, start_ptr, end_ptr, search_element):

        while(start_ptr <= end_ptr):
            mid_ptr = (start_ptr + end_ptr)//2
            if input_array[mid_ptr] == search_element:
                return mid_ptr
            elif input_array[mid_ptr] > search_element:
                end_ptr = mid_ptr - 1
                return self.binarysearch(input_array, start_ptr, end_ptr, search_element)
            elif input_array[mid_ptr] < search_element:
                start_ptr = mid_ptr + 1
                return self.binarysearch(input_array, start_ptr, end_ptr, search_element)

        if end_ptr < start_ptr:
            return end_ptr + 1
        
    def searchInsert(self, input_array, target):
        target_index = self.binarysearch(input_array, 0, len(input_array)-1, target)
        return target_index
        
s = Solution()
A = [1, 3, 5, 6]
ans = s.searchInsert(A, 7)
print(ans)



