#
# Created on Mon Jun 06 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.

If the answer does not exist return an array with a single element "-1".
First sub-array means the sub-array for which starting index in minimum.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
 B = 5

Input 2:
 A = [5, 10, 20, 100, 105]
 B = 110

Example Output
Output 1:
 [2, 3]

Output 2:
 -1

Example Explanation
Explanation 1:
 [2, 3] sums up to 5.

Explanation 2:
 No subarray sums up to required number.
'''
class Solution:
    def getSubarray(self, input_array, target):
        #returns the sub array [i,j] whose sum is equal to target value if exists, else return -1
        left = 0
        right = 0
        size = len(input_array)
        _sum = input_array[0]

        while left <= right and right < size:
            if _sum == target:
                return (left, right) #return 1-indexed sub-array whose sum = target
            elif _sum < target:
                right += 1
                if right < size:
                    _sum += input_array[right]
            else:
                _sum -= input_array[left]
                left += 1
                if left > right and left < size:
                    right += 1
                    _sum += input_array[right]
        return None

    def solve(self, A, B):
        subarrayIndices = self.getSubarray(A, B)
        if subarrayIndices:
            _from = subarrayIndices[0]
            _to = subarrayIndices[1]
            return A[_from: _to+1]
        else:
            return [-1,]

s = Solution()
A = [5, 10, 20, 100, 105]
B = 110
print(s.solve(A,B))

A = [1, 2, 3, 4, 5]
B = 5
print(s.solve(A,B))

A = [1,3,2,5,2,7]
B = 7
print(s.solve(A,B))

A = [ 42, 9, 38, 36, 48, 33, 36, 50, 38, 8, 13, 37, 33, 38, 17, 25, 50, 50, 41, 29, 34, 18, 16, 6, 49, 16, 21, 29, 41, 7, 37, 14, 5, 30, 35, 26, 38, 35, 9, 36, 34, 39, 9, 4, 41, 40, 3, 50, 27, 17, 14, 5, 31, 42, 5, 39, 38, 38, 47, 24, 41, 5, 50, 9, 29, 14, 19, 27, 6, 23, 17, 1, 22, 38, 35, 6, 35, 41, 34, 21, 30, 45, 48, 45, 37 ]
B = 100
print(s.solve(A,B))