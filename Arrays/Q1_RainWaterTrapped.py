#
# Created on Tue Apr 26 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Problem Constraints
1 <= |A| <= 100000

Input Format
First and only argument is the vector A

Output Format
Return one integer, the answer to the question

Example Input
Input 1:
    A = [0, 1, 0, 2]
Input 2:
    A = [1, 2]

Example Output
Output 1:
    1
Output 2:
    0

Example Explanation
Explanation 1:
    1 unit is trapped on top of the 3rd element.
Explanation 2:
    No water is trapped.
'''
#Approach: when we have a building of height h, we will check its maximum left and right height buildings,
# so that the rain water can be trapped.  The amount of water trapped is = min(left, right) - curr., building height
#Hint: so, 1. we will compute the maximum height of building so far from left to right = prefixHeight
#   2. similarly we also compute max., height of building so far from right to left = suffixHeight
#   3. Iterate over each building from index 1 to n-1, and compute min(left,right)  heights - curr., building height

class Solution1:
	# @param A : tuple of integers
	# @return an integer
    def trap1(self, A):
        n = len(A)
        prefixHeight = [A[0],]
        suffixHeight = [A[n-1],]

        #build prefixHeight array
        _max = A[0]
        for i in range(1, n):
            if A[i-1] > _max:
                prefixHeight.append(A[i-1])
                _max = A[i-1]
            else:
                prefixHeight.append(_max)

        #build suffixHeight array
        _max = A[n-1]
        for i in range(n-2, -1 , -1):
            if A[i+1] > _max:
                suffixHeight.insert(0, A[i+1])
                _max = A[i+1]
            else:
                suffixHeight.insert(0, _max)
        
        print(prefixHeight)
        print(suffixHeight)

        waterTrapped = 0
        #iterate through each building heights and compute how much  rain water can be trapped
        for i in range(1, n-1):
            currBuildingHeight = A[i]
            waterTrapped += max(min(prefixHeight[i], suffixHeight[i]) - currBuildingHeight, 0)
        
        return waterTrapped

#Following is optimized one
class Solution:
	# @param A : tuple of integers
	# @return an integer
    def trap(self, A):
        n = len(A)
        lIndex = 0; rIndex = n-1
        maxLeft = 0; maxRight = 0
        rainWaterTrapped = 0

        while(lIndex <= rIndex):
            if A[lIndex] <= A[rIndex]:
                if A[lIndex] >= maxLeft:
                    maxLeft = A[lIndex]
                else:
                    rainWaterTrapped += maxLeft - A[lIndex]
                
                lIndex += 1

            else:
                if A[rIndex] >= maxRight:
                    maxRight = A[rIndex]
                else:
                    rainWaterTrapped += maxRight - A[rIndex]
                
                rIndex -= 1

        return rainWaterTrapped

s = Solution()
Building_Heights = [4,2,5,7,4,2,3,6,8,2,3]
#Building_Heights = [1, 2]
#Building_Heights = [0, 1, 0, 2]
#Building_Heights = [9]
Building_Heights = [1, 0, 2, 5, 1, 0, 3, 0, 0, 7]
ans = s.trap(Building_Heights)
print(ans)