#
# Created on Thu May 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
Find the two integers that appear only once.

Problem Constraints
2 <= |A| <= 100000
1 <= A[i] <= 109

Input Format
The first argument is an array of integers of size N.

Output Format
Return an array of two integers that appear only once.

Example Input
Input 1:
    A = [1, 2, 3, 1, 2, 4]
Input 2:
    A = [1, 2]

Example Output
Output 1:
    [3, 4]
Output 2:
    [1, 2]

Example Explanation
Explanation 1:
    3 and 4 appear only once.
Explanation 2:
    1 and 2 appear only once.
'''
class Solution:
    def checkBit(self, n, i):
        if (n>>i) & 1:
            return True
        else:
            return False
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        #A is input array where it has all the numbers appear twice except two numbers, we need to return those two numbers
        #Hint: when we do XOR of all the numbers we will end up with a^b 
        #to find out a and b, if we observe the set bits of a^b it is the contribution from the bits of a,b; as the contribution from the rest elements as they appear twice its XOR will become 0
        
        #lets initialize the result two numbers
        n1 = 0
        n2 = 0

        n = len(A)
        xor = 0
        for i in range(n):
            xor ^= A[i]
        
        #check the set bit position of xor
        for p in range(32):
            if self.checkBit(xor, p):
                break
        
        #at position p the xor bit is set, so lets see what are all the numbers contribute to set this bit and what are all contribute to unset
        for i in range(n):
            if self.checkBit(A[i], p):
                n1 ^= A[i]
            else:
                n2 ^= A[i]
        if n1 < n2:
            return [n1, n2]
        else:
            return [n2, n1]

s = Solution()
A = [1, 2, 3, 1, 2, 4]
ans = s.solve(A)
print(ans)
A = [1, 2]
ans = s.solve(A)
print(ans)