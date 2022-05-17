#
# Created on Tue May 17 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a number A, we need to find the sum of its digits using recursion.

Problem Constraints
1 <= A <= 109

Input Format
The first and only argument is an integer A.

Output Format
Return an integer denoting the sum of digits of the number A.

Example Input
Input 1:
    A = 46
Input 2:
    A = 11

Example Output
Output 1:
    10
Output 2:
    2
Example Explanation
Explanation 1:
    Sum of digits of 46 = 4 + 6 = 10
Explanation 2:
    Sum of digits of 11 = 1 + 1 = 2
'''
import sys
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        #sys.setrecursionlimit(A)
        if A >= 0:
            if A == 0:
                return 0
            else:
                return (A % 10) + self.solve(A//10)

#test
s = Solution()
ans = s.solve(46)
assert ans == 10
ans = s.solve(11)
assert ans == 2