#
# Created on Thu May 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
There are certain problems which are asked in the interview to also check how you take care of overflows in your problem.
This is one of those problems.
Please take extra care to make sure that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if number of elements is as large as 105

Food for thought :
    Even though it might not be required in this problem, in some cases, you might be required to order the operations cleverly so that the numbers do not overflow.
    For example, if you need to calculate n! / k! where n! is factorial(n), one approach is to calculate factorial(n), factorial(k) and then divide them.
    Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
    Obviously approach 1 is more susceptible to overflows.
    
~~~~~~~
Problem Statement: You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
~~~~~~~
Note: Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
Note that in your output A should precede B.

Example:
Input:[3 1 2 5 3] 
Output:[3, 4] 
    A = 3, B = 4
'''
class Solution:
    def checkBit(self, n, i):
        #check if the i-th bit is set or unset
        if (n >> i) & 1:
            return True
        else:
            return False

    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        #As the numbers in array, A are ranging from 1 to n, but exactly one ele appears twice so one number in 1-n will be missing. 
        # so, we have to return that missing number and the number which appeared twice.
        #Lets say Input:[3 1 2 5 3]; n is 5.  i.e., input array is expected from 1-5 [1,2,3,4,5] 3 repeated twice and 4 is missing
        #we can add 1-n elements to the input array so that it looks like [3,1,2,5,3,  1,2,3,4,5]
        #and if we do xor of all these we will be left with 3^4 = 1 1 1
            #this 111 is the contribution from only 3 and 4 numbers.  so, if we do check for atleast one set bit of 3^4.
            #lets say at position 0 of 3^4 = 111 bit is set. lets consider the elements which are set and unset at position 0 from  [3,1,2,5,3,  1,2,3,4,5]
            #set ones at pos0-- [3,1,5,3,1,3,5] xor of all these will result = 3.
            #unset ones at pos0 - [2,2,4] xor of all these will result = 4
        #so, we got that 3,4 are the answer numbers.  But to identify which of them has appeared twice and which of them was missing in the input array
        #we know it should numbers from 1 to n; its sum will be n*(n+1)/2 
        #if we sum the input array A = [3,1,2,5,3] = 14
        #so it could be either of the two  14 - 3 + 4 or 14 - 4 + 3
        #i.e., Inputsum - doubleEle + missingEle == n*(n+1)/2 

        req_sum = n*(n+1) // 2
        input_arr_sum = sum(A)

        xor = 0
        for i in range(n):
            xor = xor ^ A[i] ^ (i+1)
        
        for p in range(n):
            #we don't even need to iterate though n bits, log(N) is sufficient
            #as anyhow we'll break as soon as we see a set bit, it doesn't matter
            if self.checkBit(xor, p):
                break
        
        #these two numbers we need to identify; ie., one is repeated twice and another one which is missing
        n1 = 0
        n2 = 0

        #let's check which numbers from 1-n and in the input array are set at bit position p; and which are all unset at bit position p
        for num in range(1, n+1):
            if self.checkBit(num, p):
                n1 ^= num
            else:
                n2 ^= num
        
        for ele in A:
            if self.checkBit(ele, p):
                n1 ^= ele
            else:
                n2 ^= ele
        
        #now to identify which among n1 and n2 is duplicated and which one is missing...
        if req_sum == input_arr_sum - n1 + n2:
            #n1 is duplicated and n2 is missing
            return [n1, n2]
        else:
            return [n2, n1]

s = Solution()
A = [3, 1, 2, 5, 3] 
ans = s.repeatedNumber(A)
assert ans == [3, 4] #print(ans)







