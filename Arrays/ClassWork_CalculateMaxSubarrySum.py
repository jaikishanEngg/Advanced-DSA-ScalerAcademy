#
# Created on Mon May 09 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
We will use Kadane's Algorithm
we use two variables
1. CumulativeSum = we will keep adding up the elements.  
If our cumulativeSum is -ve, and it doesn't make sense even after adding up the new +ve item
because say cur_sum = -10 and if the new item we're going to add is 15 then -10+15 = 5 it is going to minimize, rather it is better to start with the element 15 itself.
so, if cur_sum is -ve we will reset it to 0

2. MaximumSum = MAX ( cur_sum, max_sum)
Initialize it with A[0]
'''
class Solution:
    
    def maxSubarraySum(self, arr):
        #Approach: Kadane's algorithm
        #returns an integer, having the maximum sum of the subarray
        n = len(arr)

        max_sum = arr[0]
        cur_sum = arr[0]

        for i in range(1, n):
            if cur_sum < 0 :
                cur_sum = 0
            cur_sum += arr[i]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum

    def maxSumSubarray(self, arr):
        #Approach: Kadane's algorithm
        #returns sub-array, having the max sum
        n = len(arr)

        max_sum = arr[0]
        cur_sum = arr[0]
        
        start = 0
        end = 0

        for i in range(1, n):
            if cur_sum < 0 :
                cur_sum = 0
                if i < n-1:
                    start = i

            cur_sum += arr[i]
            if cur_sum > max_sum:
                end = i

            max_sum = max(max_sum, cur_sum)
        
        return start, end

#test case: #1
arr = [5, 6, 7, -3, 2, -10, -12, 8, 12, 21, -4, 7] 
s = Solution()
ans = s.maxSubarraySum(arr)
assert ans == 44

st, e = s.maxSumSubarray(arr)
print("MAX sum sub array of {} is {}, and the maximum sum = {}".format(arr,arr[st:e+1],ans))

#test case: #2
arr = [2, 4, -7, 10]
s = Solution()
ans = s.maxSubarraySum(arr)
assert ans == 10
st, e = s.maxSumSubarray(arr)
print("MAX sum sub array of {} is {}, and the maximum sum = {}".format(arr,arr[st:e+1],ans))

#test case: #3
arr = [-20, 10, -20, -12, 6, 5, -3, 8, -2]
s = Solution()
ans = s.maxSubarraySum(arr)
assert ans == 16
st,e = s.maxSumSubarray(arr)
print("MAX sum sub array of {} is {}, and the maximum sum = {}".format(arr,arr[st:e+1],ans))