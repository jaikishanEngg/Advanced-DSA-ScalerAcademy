#
# Created on Mon May 30 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given 2 arrays, A of size N and B of size M.
Count no.of pairs (i,j) such that A[i] > B[j]
'''
class Solution:
    def solve(self, A, B):
        A = sorted(A)
        B = sorted(B)
        n = len(A)
        m = len(B)

        count = 0

        i = j = 0
        while(i< n and j < m):
            if A[i] > B[j]:
                count += (n-i)
                j += 1
            else:
                i += 1
        
        return count

s = Solution()
A = [7, 3, 5]
B = [2, 0 ,6]
ans = s.solve(A,B)
print(ans)