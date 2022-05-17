#
# Created on Wed May 11 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a row-wise and column-wise sorted matrix A of size N * M.
Return the maximum non-empty submatrix sum of this matrix.

Problem Constraints
1 <= N, M <= 1000
-109 <= A[i][j] <= 109

Input Format
The first argument is a 2D integer array A.

Output Format
Return a single integer that is the maximum non-empty submatrix sum of this matrix.

Example Input
Input 1:-
    -5 -4 -3
A = -1  2  3
     2  2  4

Input 2:-
    1 2 3
A = 4 5 6
    7 8 9

Example Output
Output 1:-
    12
Output 2:-
    45

Example Explanation
Expanation 1:-
    The submatrix with max sum is 
        -1 2 3
         2 2 4
    Sum is 12.
Explanation 2:-
    The largest submatrix with max sum is 
        1 2 3
        4 5 6
        7 8 9
    The sum is 45.
'''
'''
Approach:
1. calculate cumSum for last column
2. calcu cumSum for last row

cal cumSum for all the other rows
	i. any index[r][c] = index[r][c] + index[r+1][c] + index[r][c+1] - index[r+1][c+1]

3. keep a track of MaxSum so far, 
'''

class Solution:
    def solve(self, A):
        n = len(A) #no.of rows
        m = len(A[0]) #no.of columns
        #initialize with suffix element (bottom right) as the input array is sorted in ascending order of row wise and col wise
        maxSum = A[n-1][m-1]

        suffixCumSumArr = [[0]*m for i in range(n)]
        suffixCumSumArr[n-1][m-1] = A[n-1][m-1]

        #calculate the suffixCumSum for last row and last column and store the results in suffixCumSumArr
        lastRow = n-1
        lastCol = m-1
        for j in range(lastCol-1, -1,  -1):
            suffixCumSumArr[lastRow][j] = suffixCumSumArr[lastRow][j+1] + A[lastRow][j]
        maxSum = max(maxSum, max(suffixCumSumArr[lastRow]))
        
        for i in range(lastRow-1, -1, -1):
            suffixCumSumArr[i][lastCol] = suffixCumSumArr[i+1][lastCol] + A[i][lastCol]
        
        for row in range(lastRow-1, -1, -1):
            for col in range(lastCol-1, -1, -1):
                suffixCumSumArr[row][col] = suffixCumSumArr[row+1][col] + suffixCumSumArr[row][col+1] + A[row][col] - suffixCumSumArr[row+1][col+1]
            maxSum = max(maxSum, max(suffixCumSumArr[row]))
        
        return maxSum

s = Solution()
A = [[-5, -4, -3],[-1, 2, 3],[2, 2, 4]]
ans = s.solve(A)
print(ans)