#
# Created on Tue May 17 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Implement pow(A, B) % C.
In other words, given A, B and C, Find (AB % C).

Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.

Problem Constraints
-109 <= A <= 109
0 <= B <= 109
1 <= C <= 109

Input Format
Given three integers A, B, C.

Output Format
Return an integer.

Example Input
A = 2, B = 3, C = 3

Example Output
2

Example Explanation
23 % 3 = 8 % 3 = 2
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A == 1 or B == 0:
            #As 1 power anything is 1.  anything power 0 is also 1
            return 1%C
        else:
            halfpower = self.pow(A, B//2, C)
            if B&1 :
                #if B is odd
                return ((halfpower % C) * (halfpower % C) * (A%C))%C
            else:
                #if B is even
                return ((halfpower % C) * (halfpower % C))%C

s = Solution()
ans = s.pow(A = 2, B = 3, C = 3)
assert ans == 2

ans = s.pow(A = 0, B = 0, C = 1)
assert ans == 0
