#
# Created on Thu Jun 23 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q3. Container With Most Water

Problem Description
Given n non-negative integers A[0], A[1], ..., A[n-1] , where each represents a point at coordinate (i, A[i]).
N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

Problem Constraints
0 <= N <= 105
1 <= A[i] <= 105

Input Format
Single Argument representing a 1-D array A.

Output Format
Return single Integer denoting the maximum area you can obtain.

Example Input
Input 1:
A = [1, 5, 4, 3]

Input 2:
A = [1]

Example Output
Output 1:
 6

Output 2:
 0

Example Explanation
Explanation 1:
5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 
So total area = 3 * 2 = 6

Explanation 2:
No container is formed.
'''
class Solution:
	# @param A : list of integers
	# @return an integer
    def maxArea(self, input_array):
        size = len(input_array)
        p1 = 0
        p2 = size - 1
        max_water_accumulated = 0
        while(p1 < size and p2 >= 0):
            width = p2 - p1
            if input_array[p1] < input_array[p2]:
                height = input_array[p1]
                p1 += 1
            else:
                height = input_array[p2]
                p2 -= 1

            if p1 == p2:
                p1 += 1               
            
            water_accumulated = width * height
            max_water_accumulated = max(max_water_accumulated, water_accumulated)

        return max_water_accumulated

s = Solution()
A = [1, 5, 4, 3]
ans = s.maxArea(A)
assert ans == 6

A = [1]
ans = s.maxArea(A)
assert ans == 0




