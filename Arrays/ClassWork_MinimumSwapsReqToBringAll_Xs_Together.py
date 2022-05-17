#
# Created on Tue May 10 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given an array and a number x, count the minimum no.of swaps req to bring all x's together.
A = 10, 4, 8, 7, 8, 3, 8, -1, 8, 8.  and x = 8
'''
class Solution:
    def solve(self, A, x):
        #Using sliding window protocol technique we will solve this problem

        #first count the no.of x's in A. so that we will set the window size to it to bring all x's in one window
        c = 0
        for i in range(len(A)):
            if A[i] == x:
                c += 1
        
        #Build first window and count the no.of x's in it
        xCount = 0
        minSwaps = None #answer
        for i in range(c):
            if A[i] == x:
                xCount += 1
        minSwaps = c - xCount


        #scan/slide through the subsequent windows and count the no.of x's in each window 
        #the next window start and end values can go from 1 to n-1
        wStart = 1
        wEnd = wStart + c - 1
        while wStart <= len(A) - c and wEnd < len(A):
            if A[wStart - 1] == x:
                xCount -= 1
            if A[wEnd] == x:
                xCount += 1
            curSwaps = c - xCount
            minSwaps = min(curSwaps, minSwaps)
            wStart += 1
            wEnd += 1
        return minSwaps

s = Solution()
A = [10, 4, 8, 7, 8, 3, 8, -1, 8, 8]
ans = s.solve(A, x = 8)
assert ans == 2
#print(ans) #2



