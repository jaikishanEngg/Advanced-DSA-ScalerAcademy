#
# Created on Tue May 10 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given a matrix, find maximum submatrix sum such that 
    the submatrix can start anywhere and end anywhere (No constraints)
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
                
            