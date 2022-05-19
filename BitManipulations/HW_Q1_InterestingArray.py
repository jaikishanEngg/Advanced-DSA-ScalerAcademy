#
# Created on Thu May 19 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You have an array A with N elements. We have two types of operation available on this array :
We can split an element B into two elements, C and D, such that B = C + D.
We can merge two elements, P and Q, to one element, R, such that R = P ^ Q i.e., XOR of P and Q.
You have to determine whether it is possible to convert array A to size 1, containing a single element equal to 0 after several splits and/or merge?

Problem Constraints
1 <= N <= 100000
1 <= A[i] <= 106

Input Format
The first argument is an integer array A of size N.

Output Format
Return "Yes" if it is possible otherwise return "No".

Example Input
Input 1:
    A = [9, 17]
Input 2:
    A = [1]

Example Output
Output 1:
    Yes
Output 2:
    No

Example Explanation
Explanation 1:
 Following is one possible sequence of operations -  
 1) Merge i.e 9 XOR 17 = 24  
 2) Split 24 into two parts each of size 12  
 3) Merge i.e 12 XOR 12 = 0  
 As there is only 1 element i.e 0. So it is possible.

Explanation 2:
 There is no possible way to make it 0.
'''
class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        n = len(A) #Assuming n > 0
        if(n == 0):
            return "No"
        if(n == 1):
            if(A[0] == 0):
                return "Yes"
            else:
                return "No"
        
        else:
            #if n > 1
            xor = 0
            concat = 0
            for i in range(n):
                xor = xor ^ A[i]
                concat = concat + A[i]
            if(xor&1 == 0 or concat&1 ==0):
                return "Yes"
            else:
                return "No"

#Test

s = Solution()
A = [9, 17]
ans = s.solve(A)
assert ans == "Yes"
A = [1]
ans = s.solve(A)
assert ans == "No"