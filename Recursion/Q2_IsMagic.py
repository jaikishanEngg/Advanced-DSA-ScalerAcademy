#
# Created on Tue May 17 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a number A, check if it is a magic number or not.
A number is said to be a magic number if the sum of its digits is calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1, then the number is a magic number.

Problem Constraints
1 <= A <= 109

Input Format
The first and only argument is an integer A.

Output Format
Return an 1 if the given number is magic else return 0.

Example Input
Input 1:
    A = 83557
Input 2:
    A = 1291

Example Output
Output 1:
    1
Output 2:
    0

Example Explanation
Explanation 1:
 Sum of digits of (83557) = 28
 Sum of digits of (28) = 10
 Sum of digits of (10) = 1. 
 Single digit is 1, so it's a magic number. Return 1.

Explanation 2:
 Sum of digits of (1291) = 13
 Sum of digits of (13) = 4
 Single digit is not 1, so it's not a magic number. Return 0.
'''
class Solution:
    def sumOfDigits(self, A):
        #this method will return the sum of the digits of a number
        if A == 0:
            return 0
        else:
            return (A % 10) + self.sumOfDigits(A//10)
    
    # @param A : integer
    # @return an integer
    def solve(self, A):
        #we will return True(1) if the recursive sum of the digits is 1, else return False(0)
        #Here we will make use of the sumOfDigits method
        if A == 1:
            return 1
        else:
            n = self.sumOfDigits(A)
            while n > 9:
                n = self.sumOfDigits(n)
            if n == 1:
                return 1
            else:
                return 0

#test
s = Solution()
ans = s.solve(83557)
assert ans == 1

ans = s.solve(1291)
assert ans == 0