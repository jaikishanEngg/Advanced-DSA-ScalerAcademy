#
# Created on Mon Jun 06 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an array of integers A and an integer B, find and return the maximum value K 
such that there is no subarray in A of size K with the sum of elements greater than B.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9

Input Format
The first argument given is the integer array A.
The second argument given is integer B.

Output Format
Return the maximum value of K (sub array length).

Example Input
Input 1:
    A = [1, 2, 3, 4, 5]
    B = 10

Input 2:
    A = [5, 17, 100, 11]
    B = 130

Example Output
Output 1:
    2
Output 2:
    3

Example Explanation
Explanation 1:
    Constraints are satisfied for maximal value of 2.

Explanation 2:
    Constraints are satisfied for maximal value of 3.

See Expected Output
Your input
4 5 17 100 11 #where 4 is the size of array
129 #max sum of the sub-array
Output
3 #its the minimum size of sub-array with sum <= 129 (i.e., 17, 100, 11 gives sum of 129 <= 129. so size 3)
'''
class Solution:
    def getMaxSubarraySumOfLengthK(self, input_array, k):
        size = len(input_array)
        maxSum = None
        if k == 1:
            return max(input_array)
        elif k > 1:
            _sum = 0
            for i in range(k):
                _sum += input_array[i]
            maxSum = _sum
            #sliding window approach
            i = 1
            while i <= size-k :
                _sum = _sum - input_array[i-1] + input_array[i-1+k]
                maxSum = max(maxSum, _sum)
                i += 1
        return maxSum

    def getMaxSubarrayLength(self, input_array, target, lPtr, rPtr, ans):
        #return maximum subarray length whose sum is <= target
        #using binary search approach we will solve this.
        #lPtr and rPtr representing the length of sub-array
        
        while lPtr <= rPtr:
            mid = (lPtr + rPtr)//2
            subarraySum = self.getMaxSubarraySumOfLengthK(input_array, mid)
            if subarraySum == target:
                return mid
            elif subarraySum < target:
                ans = mid #possible answer
                #increase the length
                lPtr = mid + 1
                return self.getMaxSubarrayLength(input_array, target, lPtr, rPtr, ans)
            else:
                rPtr = mid - 1
                return self.getMaxSubarrayLength(input_array, target, lPtr, rPtr, ans)
        
        return ans

    def solve(self, A, B):
        return self.getMaxSubarrayLength(A, B, 0, len(A),-1)

s = Solution()
A = [1, 2, 3, 4, 5]
B = 10
print(s.solve(A, B))

A = [5, 17, 100, 11]
B = 130
print(s.solve(A, B))

A = [5, 17, 100, 11]
B = 129
print(s.solve(A, B))

