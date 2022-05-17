#
# Created on Tue May 10 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
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