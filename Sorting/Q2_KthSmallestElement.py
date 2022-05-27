#
# Created on Wed May 25 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Find the Bth smallest element in given array A .

NOTE: Users should try to solve it in less than equal to B swaps.

Problem Constraints
1 <= |A| <= 100000
1 <= B <= min(|A|, 500)
1 <= A[i] <= 109

Input Format
    The first argument is an integer array A.
    The second argument is integer B.

Output Format
    Return the Bth smallest element in given array.

Example Input
Input 1:
    A = [2, 1, 4, 3, 2]
    B = 3

Input 2:
    A = [1, 2]
    B = 2

Example Output
Output 1:
    2

Output 2:
    2

Example Explanation
Explanation 1:
    3rd element after sorting is 2.
Explanation 2:
    2nd element after sorting is 2.
'''
class Solution:
    # @param A : tuple of integers
	# @param B : integer
	# @return an integer
    def kthsmallest(self, input_array, k):
        #return the k-th smallest element of the input array
        #we will use selection sort algorithm (stable version)
        input_array = list(input_array)
        size = len(input_array)

        for i in range(size):
            minElement = input_array[i] #lets initialize the first element as minimum
            minElementIndex = None
            for j in range(i+1, size):
                if input_array[j] < minElement:
                    minElement = input_array[j]
                    minElementIndex = j
            
            if minElementIndex:
                #lets insert the minimum element at its correct place than swapping it.
                #and shift all the other element by one position
                for p in range(minElementIndex-1, i-1, -1):
                    input_array[p+1] = input_array[p]
            
                input_array[i] = minElement
            
            if i == k-1:
                return input_array[i]

s = Solution()
A = [2, 1, 4, 3, 2]
B = 3
ans = s.kthsmallest(A,B)
print(ans)

A = [1, 2]
B = 2
ans = s.kthsmallest(A,B)
print(ans)

