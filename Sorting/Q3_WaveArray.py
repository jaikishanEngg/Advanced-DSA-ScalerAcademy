#
# Created on Wed Jun 01 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given an array of integers A, sort the array into a wave-like array and return it.
In other words, arrange the elements into a sequence such that

a1 >= a2 <= a3 >= a4 <= a5..... 
NOTE: If multiple answers are possible, return the lexicographically smallest one.

Problem Constraints
1 <= len(A) <= 106
1 <= A[i] <= 106

Input Format
The first argument is an integer array A.

Output Format
Return an array arranged in the sequence as described.

Example Input
Input 1:
    A = [1, 2, 3, 4]

Input 2:
    A = [1, 2]

Example Output
Output 1:
    [2, 1, 4, 3]

Output 2:
    [2, 1]

Example Explanation
Explanation 1:
    One possible answer : [2, 1, 4, 3]
    Another possible answer : [4, 1, 3, 2]
    First answer is lexicographically smallest. So, return [2, 1, 4, 3].

Explanation 1:
    Only possible answer is [2, 1].

Intuition:
Basically a wave looks like 
either A[i-1] < A[i] > A[i+1] that is 1 < 5 > 3
or A[i-1] > A[i] < A[i+1] that is 4 > 2 < 5

lets say if we have a sorted array in ascending order A = [1,2,3,4,5]
interchanging the consecutive pairs will make it a wave array 
swap/interchange (1,2) will give [2,1] then (3,4) => [4,3] then only one element 5 is left 
resultant array will looks like = [2,1, 4,3, 5] and this is a wave array

or if we have a sorted array in descending order A = [5, 4, 3, 2, 1]
[4,5,  2,3,  1]  this is also a wave.
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, input_array):
        input_array.sort()
        size = len(input_array)

        if size > 1:
            for i in range(1, size, 2):
                #interchange/swap the consecutive elements
                input_array[i], input_array[i-1] = input_array[i-1], input_array[i]

        return input_array

obj = Solution()
input_array = [1, 2, 3, 4]
#input_array = [1,]
#input_array = [ 5, 1, 3, 2, 4 ]
wave_array = obj.wave(input_array)
print(wave_array)


        
