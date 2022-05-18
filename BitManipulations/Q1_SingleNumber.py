#
# Created on Wed May 18 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.

NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Problem Constraints
2 <= |A| <= 2000000
0 <= A[i] <= INTMAX

Input Format
The first and only argument of input contains an integer array A.

Output Format
Return a single integer denoting the single element.

Example Input
Input 1:
    A = [1, 2, 2, 3, 1]
Input 2:
    A = [1, 2, 2]

Example Output
Output 1:
    3
Output 2:
    1

Example Explanation
Explanation 1:
    3 occurs once.
Explanation 2:
    1 occurs once.
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        #Hint: we can make use of XOR operator. As a^a = 0, 
        # as every element is occuring twice when we do xor of same element with itself, results into 0 
        # and then 0^b = b
        
        n = len(A)
        ans = 0
        for i in range(n):
            ans ^= A[i]
        return ans

s = Solution()
A = [1, 2, 2, 3, 1]
ans = s.singleNumber(A)
assert ans == 3
A = [1, 2, 2]
ans = s.singleNumber(A)
assert ans == 1
A = [3]
ans = s.singleNumber(A)
assert ans == 3




