#
# Created on Wed May 11 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a N * M 2D matrix A. Find the maximum sum sub-matrix from the matrix A. Return the Sum.

Problem Constraints
1 <= N, M <= 300
-104 <= A[i][j] <= 104

Input Format
The first argument is a 2D Integer array A.

Output Format
Return the sum of the maximum sum sub-matrix from matrix A.

Example Input
Input 1:-
A = -6 -6
   -29 -8
    3 -8
   -15  2
    25 25
    20 -5

Input 2:-
A = -17 -2
     20 10

Example Output
Output 1:-
    65
Output 2:-
    30

Example Explanation
Explanation 1:-
    The submatrix 
    25 25
    20 -5
    has the highest submatrix sum 65.
Explanation 2:-
    The submatrix 
    20 10
    has the highest sub matrix sum 30.
'''
class Solution:
    def maxSubArray(self, A):
        #Kadane's algorithm to find the maxSubarraySum
        n = len(A)
        cumulativeSum = A[0]
        maxSum = A[0]

        if cumulativeSum < 0:
            cumulativeSum = 0

        for i in range(1, n):
            cumulativeSum += A[i]
            maxSum = max(cumulativeSum, maxSum)
            if cumulativeSum < 0:
                cumulativeSum = 0
        
        return maxSum

    def solve(self, A):
        n = len(A) #no.of rows
        m = len(A[0]) #no.of columns
        maxSum = A[0][0]

        for startrow in range(n):
            curMaxSubArrSum = A[0][0]        
            colPrefixSumArr = [0]*m
            for endrow in range(startrow, n):
                for j in range(m):
                    colPrefixSumArr[j] += A[endrow][j]
                #now columnwise prefix ready for each row
                #apply kadane's algorithm on each colPrefixSum generated, and maintain the maxSum possible as a result variable
                curMaxSubArrSum = self.maxSubArray(colPrefixSumArr)
                maxSum = max(maxSum, curMaxSubArrSum)
        
        return maxSum

#test
s = Solution()
A = [[1,   3, -10, -3,  4],
     [-3, -4,   2, -2, 10],
     [2,   6,  -9,  6, -1],
     [-4,  2,   4, -3, -8]]
ans = s.solve(A)
print(ans)
                
            