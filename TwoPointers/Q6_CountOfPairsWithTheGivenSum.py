#
# Created on Thu Jun 23 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q6. Count of pairs with the given sum
Given a sorted array of distinct integers A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the number of pairs for which sum is equal to B.

Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
1 <= B <= 10^9

For Example
Input 1:
    A = [1, 2, 3, 4, 5]
    B = 5

Output 1:
    2

Input 2:
    A = [5, 10, 20, 100, 105]
    B = 110
Output 2:
    2
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, input_array, X):
        return self.countOfPairsWithSumX(input_array, X)
    
    def countOfPairsWithSumX(self, input_array, X):
        #input_array is a sorted array
        #returns the number of pairs with sum X  (A[i], A[j]) such that i != j 
        uniquePairs = dict()
        pairCount = 0
        size = len(input_array)

        p1 = 0
        p2 = size - 1

        while p1 < p2:
            if input_array[p1] + input_array[p2] == X:
                if (input_array[p1], input_array[p2]) not in uniquePairs:
                    pairCount += 1
                    uniquePairs[(input_array[p1], input_array[p2])] = True
                p1 += 1
            
            elif input_array[p1] + input_array[p2] > X:
                p2 -= 1
            
            else:
                p1 += 1

        return pairCount

s = Solution()
A = [1, 2, 3, 4, 5]
B = 5
ans = s.solve(A, B)
assert ans == 2

A = [5, 10, 20, 100, 105]
B = 110
ans = s.solve(A, B)
assert ans == 2

