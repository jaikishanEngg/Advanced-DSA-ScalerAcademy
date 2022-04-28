#
# Created on Thu Apr 28 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.
The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.
Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
Find and return the required subarray.

NOTE:
    1. If there is a tie, then compare with segment's length and return segment which has maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.

Input Format:
    The first and the only argument of input contains an integer array A, of length N.
Output Format:
    Return an array of integers, that is a subarray of A that satisfies the given conditions.
Constraints:
    1 <= N <= 1e5
    -INT_MAX < A[i] <= INT_MAX
Examples:
Input 1:
    A = [1, 2, 5, -7, 2, 3]
Output 1:
    [1, 2, 5]

Explanation 1:
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3].

Input 2:
    A = [10, -1, 2, 3, -4, 100]
Output 2:
    [100]

Explanation 2:
    The three sub-arrays are [10], [2, 3], [100].
    The answer is [100] as its sum is larger than the other two.
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        n = len(A)

        #initialize the start and end index of maxNonNegativeSet indices
        start = -1
        end = -1

        #Initialize maxSum and CurrentSum
        maxSum = A[0]
        curSum = None

        #Its a current index (start index)
        curr_i = None

        for i in range(n):
            #whenever I see a +ve element then I'll do the logical things
            if A[i] >= 0:
                if(curSum == None):
                    curSum = A[i]
                    curr_i = i  #Assign the fresh postive elements index to current start index                    
                else:
                    curSum += A[i]

                if curSum >= maxSum:
                    #Wheneever we get currentsum >= maxSum we will have to check the following
                        #1. If curSum > maxSum then directly update the start and end indices
                        #2. if curSum == maxSum then
                            #2.i. check the lengths if the lenth of current subset  is > than previous set length then update the start and end indices
                            #other wise we don't need to update the start and end indices

                    if(start == -1 and end == -1):
                        start = curr_i
                        end = i
                    
                    if(curSum == maxSum):
                        curLen = i - curr_i + 1
                        preLen = end - start + 1
                        if curLen > preLen:
                            start = curr_i
                            end = i
                            maxSum = curSum

                    if curSum > maxSum:
                        start = curr_i
                        end = i
                        maxSum = curSum

            #if the element is negative then I'll simply assign curSum to None
            else:
                curSum = None

        if maxSum < 0:
            return []
        else:
            return A[start:end+1]
        
s = Solution()
#Test cases:
A = [10, -1, 2, 3, -4, 100] #[100]
#A = [-1, -2, -3] #[]
#A = [10, 20, -30, -40, -50] #[10,20]
#A = [1, 2, 5, -7, 2, 3] #[1, 2, 5]
ans = s.maxset(A)
print(ans)