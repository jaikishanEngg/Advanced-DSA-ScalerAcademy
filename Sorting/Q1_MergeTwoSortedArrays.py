#
# Created on Wed May 25 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.

Problem Constraints
-1010 <= A[i], B[i] <= 1010

Input Format
First Argument is a 1-D array representing A.
Second Argument is also a 1-D array representing B.

Output Format
Return a 1-D vector which you got after merging A and B.

Example Input
Input 1:
    A = [4, 7, 9 ]
    B = [2, 11, 19 ]

Input 2:
    A = [1]
    B = [2]

Example Output
Output 1:
    [2, 4, 7, 9, 11, 19]
Output 2:
    [1, 2]

Example Explanation
Explanation 1:
    Merging A and B produces the output as described above.
Explanation 2:
     Merging A and B produces the output as described above.
'''
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def merge(self, arr1, arr2):
        size1 = len(arr1)
        size2 = len(arr2)

        output = [] #this is the output array, merged arr1 and arr2

        #lets have two pointers pointing array1 and array2.
        a = 0
        b = 0

        while a != size1 and b != size2:
            if arr1[a] < arr2[b]:
                output.append(arr1[a])
                a += 1
            elif arr1[a] > arr2[b]:
                output.append(arr2[b])
                b += 1
            else:
                output.append(arr1[a])
                output.append(arr2[b])
                a += 1
                b += 1
        
        if a == size1:
            for ele in arr2[b:]:
                output.append(ele)
        elif b == size2:
            for ele in arr1[a:]:
                output.append(ele)
            
        return output

    def solve(self, arr1, arr2):
        return self.merge(arr1, arr2)