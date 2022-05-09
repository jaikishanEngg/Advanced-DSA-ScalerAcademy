#
# Created on Mon May 09 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a matrix of integers A of size N x M and multiple queries Q, for each query, find and return the submatrix sum.

Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.

NOTE:
Rows are numbered from top to bottom, and columns are numbered from left to right.
Sum may be large, so return the answer mod 10^9 + 7.


Problem Constraints
1 <= N, M <= 1000
    -100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M

Input Format
The first argument given is the integer matrix A.
The second argument given is the integer array B.
The third argument given is the integer array C.
The fourth argument given is the integer array D.
The fifth argument given is the integer array E.
(B[i], C[i]) represents the top left corner of the i'th query.
(D[i], E[i]) represents the bottom right corner of the i'th query.

Output Format
Return an integer array containing the submatrix sum for each query.

Example Input
Input 1:
 A = [   [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]   ]
 B = [1, 2]
 C = [1, 2]
 D = [2, 3]
 E = [2, 3]

Input 2:
 A = [   [5, 17, 100, 11]
         [0, 0,  2,   8]    ]
 B = [1, 1]
 C = [1, 4]
 D = [2, 2]
 E = [2, 4]

Example Output
Output 1:
    [12, 28]
Output 2:
    [22, 19]

Example Explanation
Explanation 1:

 For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
 For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.
Explanation 2:

 For query 1: Submatrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
 For query 2: Submatrix contains elements: 11 and 8. So, their sum is 19.
'''
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        #calculate 2-D prefix sum of the input 2-D array A
        rows = len(A)
        cols = len(A[0])
        prefixSumArr = A

        #perform row prefix sum first
        for r in range(rows):
            for c in range(1, cols):
                prefixSumArr[r][c] = prefixSumArr[r][c-1] + A[r][c]
        
        #peform col prefix sum next
        for c in range(cols):
            for r in range(1, rows):
                prefixSumArr[r][c] = prefixSumArr[r-1][c] + A[r][c]

        #print(prefixSumArr)
        #we have to find the sum of sub-matrix from (i,j) to (p,q)
        #per the constraints (i,j) = (B[i],C[i]) and (p,q) = (D[i], E[i])

        ans = []

        for q in range(len(B)):
            #As the inputs are 1-indexed make it 0-indexed by subtracting 1
            i = B[q] - 1;            j = C[q] - 1
            p = D[q] - 1 ;           q = E[q] - 1

            #per the constraints, if the sum is large use modulo 10^9 + 7

            _sum = prefixSumArr[p][q] % (10**9 + 7)

            #we know (a + b) % m = (a % m + b % m) % m
            #and (a - b) % m = ((a % m) - (b % m) + m ) % m
            #applied the same formula in the below _sum expressions.

            if i > 0:
                _sum = (_sum % (10**9 + 7) - (prefixSumArr[i - 1][q] % (10**9 + 7)) + (10**9 + 7)) % (10**9 + 7)
            if j > 0:
                _sum = (_sum % (10**9 + 7) - (prefixSumArr[p][j - 1] % (10**9 + 7)) + (10**9 + 7)) % (10**9 + 7)
            
            if i > 0 and j > 0:
                _sum = (_sum % (10**9 + 7) + prefixSumArr[i - 1][j - 1] % (10**9 + 7)) % (10**9 + 7)
                
            ans.append(_sum)

        return ans

