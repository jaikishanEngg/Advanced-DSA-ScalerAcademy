#
# Created on Thu Apr 28 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :

Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
    A: For the purpose of this question, YES
Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
    A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

Problem Constraints
1 <= size of the array <= 1000000

Input Format
First argument is an array of digits.

Output Format
    Return the array of digits after adding one.

Example Input
Input 1:
    [1, 2, 3]
Example Output
    Output 1:
    [1, 2, 4]

Example Explanation
Explanation 1:
    Given vector is [1, 2, 3].
    The returned vector should be [1, 2, 4] as 123 + 1 = 124.
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)

        firstNonZeroIndex = -1
        #find the index of first non-zero element
        for index in range(n):
            if A[index] != 0:
                firstNonZeroIndex = index
                break
        
        if firstNonZeroIndex == -1:
            return [1,]
        else:
            sum = A[n-1] + 1
            carry = sum // 10
            sum = sum % 10
            A[n-1] = sum

            for i in range(n-2, firstNonZeroIndex - 1, -1):
                sum = carry + (A[i])
                carry = sum // 10
                sum = sum % 10

                A[i] = sum
            
            if carry:
                return [1,] + A[firstNonZeroIndex:]
            else:
                return A[firstNonZeroIndex:]

        
s = Solution()
#Test cases
A = [0,0,0,0,9] # [1, 0]
A = [9,8,9] # [9, 9, 0]
A = [9,9,9] # [1, 0, 0, 0]
A = [0,0,0,0] # [1]
ans = s.plusOne(A)
print(ans)
