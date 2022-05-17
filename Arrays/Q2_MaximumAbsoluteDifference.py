#
# Created on Thu May 12 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You are given an array of N integers, A1, A2, …. AN.
Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

Problem Constraints
1 <= N <= 100000
-109 <= A[i] <= 109

Input Format
First argument is an integer array A of size N.

Output Format
Return an integer denoting the maximum value of f(i, j).

Example Input
Input 1:
    A = [1, 3, -1]
Input 2:
    A = [2]

Example Output
Output 1:
    5
Output 2:
    0

Example Explanation
Explanation 1:
    f(1, 1) = f(2, 2) = f(3, 3) = 0
    f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
    f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
    f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
    So, we return 5.
Explanation 2:
    Only possibility is i = 1 and j = 1. That gives answer = 0.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArrNaiveApproach(self, A):
        #this is a naive approach and O(n^2) will be the time
        n = len(A)
        if(n == 1):
            return 0
        else:
            ans = abs(A[0] - A[1]) #initialize
            for i in range(n):
                for j in range(i+1, n):
                    ans = max(ans, abs(A[i] - A[j]) + abs(i - j))
            return ans
    
    def maxArr(self, A):
        '''
        The approach we're following is, for 
        (i,j) = |A[i] - A[j]| + |i - j|

        case 1: when A[i] < A[j] and i < j
        then -A[i] + A[j] -i + j => A[j]+j - (A[i] + i)

        case 2: when A[i] > A[j] and i > j
        then A[i] - A[j] + i - j => A[i]+i - (A[j] + j)
        #######################case 1 and case2 are same.

        case 3: when A[i] > A[j] and i < j
        then A[i] - A[j] - i + j => A[i]-i - (A[j] - j)

        case 4: when A[i] < A[j] and i > j
        then A[j] - A[i] + i - j => A[j]-j - (A[i] - i)
        #######################case 3 and case 4 are same.
        
        As we are computing the absolute difference, a-b.  It can be max only when a is very large while b is minimum.
        '''
        n = len(A)
        if n == 1:
            return 0
        else:
            max1 = - float('inf')
            min1 = float('inf')
            max2 = - float('inf')
            min2 = float('inf')

            for i in range(n):
                j = i + 1
                max1 = max(max1, A[i] + j)
                min1 = min(min1, A[i] + j)

                max2 = max(max2, A[i] - j)
                min2 = min(min2, A[i] - j)
            
            candidate1 = max1 - min1
            candidate2 = max2 - min2

            return max(candidate1, candidate2)

                

s = Solution()
A = [1, 3, -1]
#A= [2,]                    
ans = s.maxArr(A)
print(ans)


