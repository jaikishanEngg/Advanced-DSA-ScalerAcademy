#
# Created on Fri Jun 03 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a sorted array of integers A(0 based index) of size N, find the starting and the ending position of a given integer B in array A.
Your algorithm's runtime complexity must be in the order of O(log n).
Return an array of size 2, such that the first element = starting position of B in A and the second element = ending position of B in A, if B is not found in A return [-1, -1].

Problem Constraints
1 <= N <= 106
1 <= A[i], B <= 109

Input Format
    The first argument given is the integer array A.
    The second argument given is the integer B.

Output Format
    Return an array of size 2, such that the first element = starting position of B in A and the second element = the ending position of B in A if B is not found in A return [-1, -1].

Example Input
Input 1:
    A = [5, 7, 7, 8, 8, 10]
    B = 8
Input 2:
    A = [5, 17, 100, 111]
    B = 3

Example Output
Output 1:
    [3, 4]
Output 2:
    [-1, -1]

Example Explanation
Explanation 1:
 The first occurence of 8 in A is at index 3.
 The second occurence of 8 in A is at index 4.
 ans = [3, 4]

Explanation 2:
 There is no occurence of 3 in the array.
'''
class Solution:
    def firstOccuranceOfTarget(self, input_array, start_ptr, end_ptr, target, first_occurance_index):
        #Given a sorted input_array, return the index of the first occurance of the target element
        #Note: target will definitely exists in the input_array, we already performed this check
        
        while start_ptr <= end_ptr:
            mid = (start_ptr + end_ptr)//2
            if input_array[mid] == target:
                first_occurance_index = min(first_occurance_index, mid)
                end_ptr = mid - 1
                return self.firstOccuranceOfTarget(input_array, start_ptr, end_ptr, target, first_occurance_index)
            elif input_array[mid] < target:
                start_ptr = mid + 1
                return self.firstOccuranceOfTarget(input_array, start_ptr, end_ptr, target, first_occurance_index)
            else:
                end_ptr = mid - 1
                return self.firstOccuranceOfTarget(input_array, start_ptr, end_ptr, target, first_occurance_index)
        
        return first_occurance_index
    
    def lastOccuranceOfTarget(self, input_array, start_ptr, end_ptr, target, last_occurance_index):
        #Given a sorted input_array, return the index of the first occurance of the target element
        #Note: target will definitely exists in the input_array, we already performed this check
        
        while start_ptr <= end_ptr:
            mid = (start_ptr + end_ptr)//2
            if input_array[mid] == target:
                if last_occurance_index:
                    last_occurance_index = max(last_occurance_index, mid)
                else:
                    last_occurance_index = mid
                start_ptr = mid + 1
                return self.lastOccuranceOfTarget(input_array, start_ptr, end_ptr, target, last_occurance_index)
            elif input_array[mid] < target:
                start_ptr = mid + 1
                return self.lastOccuranceOfTarget(input_array, start_ptr, end_ptr, target, last_occurance_index)
            else:
                end_ptr = mid - 1
                return self.lastOccuranceOfTarget(input_array, start_ptr, end_ptr, target, last_occurance_index)
        
        return last_occurance_index

    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, input_array, target):
        #This method searches for the target element in the input_array and if it exists then 
        # returns the first and end index of its occurance, if the element doesn't exists then return -1, -1

        size = len(input_array)
        start_ptr = 0
        end_ptr = size - 1 
        first_occurance_of_target = self.firstOccuranceOfTarget(input_array, start_ptr, end_ptr, target, size)
        last_occurance_of_target = self.lastOccuranceOfTarget(input_array, start_ptr, end_ptr, target, -1)
        if first_occurance_of_target != size or last_occurance_of_target != -1:
            return [first_occurance_of_target, last_occurance_of_target]
        else:
            #if the element doesn't exists in the input_array, then return the range as -1,-1
            return [-1, -1]


s = Solution()
A = [5, 7, 7, 8, 8, 10]
B = 8
ans = s.searchRange(A, B)
print(ans)
A = [5, 17, 100, 111]
B = 3
ans = s.searchRange(A, B)
print(ans)
