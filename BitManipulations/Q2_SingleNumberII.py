#
# Created on Wed May 18 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an array of integers, every element appears thrice except for one, which occurs once.
Find that element that does not appear thrice.

NOTE: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Problem Constraints
2 <= A <= 5*106
0 <= A <= INTMAX

Input Format
First and only argument of input contains an integer array A.

Output Format
Return a single integer.

Example Input
Input 1:
    A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Input 2:
    A = [0, 0, 0, 1]

Example Output
Output 1:
    4
Output 2:
    1

Example Explanation
Explanation 1:
 4 occurs exactly once in Input 1.
 1 occurs exactly once in Input 2.
'''
class Solution:
    def checkBit(self, n, i):
        #return True if i-th bit is set, else return False
        n = n >> i
        if n & 1:
            return True
        else:
            return False

	# @param A : tuple of integers
	# @return an integer
    def singleNumber(self, A):
        #As here every element in array occurs three times except one element, we need to find that one element
        #As every ele occurs 3 times, when we add up all of them the contribution at each bit will be 3 times
        #and at each bit of the sum, if we perform %3 then we will get the contribution of the remaining single occurance element, to the sum
        n = len(A)

        #lets sum all the individual set bits
        #Assuming all the numbers in the array are 32-bit integers
        ans = 0
        for i in range(32):
            sum_of_bit_i = 0
            for j in range(n):
                #count the set bits at ith pos for each ele in array
                if self.checkBit(A[j], i):
                    sum_of_bit_i += 1
            if sum_of_bit_i%3 != 0:
                ans = ans | (1 << i)
        
        return ans

#test 
s = Solution()
A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
ans = s.singleNumber(A)
assert ans == 4 #print(ans)
A = [0, 0, 0, 1]
ans = s.singleNumber(A)
assert ans == 1 #print(ans)





