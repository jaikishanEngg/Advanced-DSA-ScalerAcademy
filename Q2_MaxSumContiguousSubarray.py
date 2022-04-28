#
# Created on Thu Apr 28 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.

Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000

Input Format
The first and the only argument contains an integer array, A.

Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.

Example Input
Input 1:
    A = [1, 2, 3, 4, -10] 
Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 

Example Output
Output 1:
    10 
Output 2:
    6 

Example Explanation
Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6. 
'''
#Hint: we use Kadane's algorithm to solve the problem
'''
we will use two variables 1.CumulativeSum 2.MaxSum
i. whenever we see a negative value we see if the cumulative sum is going to be negative then it doesn't make sense even after we encounter the next element as positive we will get small number on adding it, rather it is better to start from that positive number only
ii. if we get positive cumalativeSum on considering that negative num, then we may hope that there could be some subarray giving max sum. so, we can consider
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
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

s = Solution()
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
ans = s.maxSubArray(A)
print(ans)


