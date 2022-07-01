#
# Created on Mon Jun 06 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an integer A.
Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).
DO NOT USE SQRT FUNCTION FROM THE STANDARD LIBRARY.

NOTE: Do not use the sqrt function from the standard library. Users are expected to solve this in O(log(A)) time.

Problem Constraints
0 <= A <= 1010

Input Format
The first and only argument given is the integer A.

Output Format
Return floor(sqrt(A))

Example Input
Input 1:
    11
Input 2:
    9

Example Output
Output 1:
    3
Output 2:
    3

Example Explanation
Explanation:

 When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
 When A = 9 which is a perfect square of 3, so we return 3.
'''
class Solution:
    def sqrt_binarySearch(self, N, left, right, ans):
        while left <= right:
            mid = (left + right)//2
            if mid*mid == N:
                return mid
            elif mid*mid < N:
                #go right
                left = mid + 1
                ans = self.sqrt_binarySearch(N, left, right, mid)
                return ans
            else:
                #go left
                right = mid - 1
                ans = self.sqrt_binarySearch(N, left, right, ans) 
                return ans
        return ans
    # @param A : integer
    # @return an integer
    def sqrt(self, N):
        #return square root of N, floor value
        return self.sqrt_binarySearch(N, 1, N, (1+N)//2)

s = Solution()
assert s.sqrt(29) == 5
assert s.sqrt(25) == 5
assert s.sqrt(37) == 6
assert s.sqrt(0) == 0
        