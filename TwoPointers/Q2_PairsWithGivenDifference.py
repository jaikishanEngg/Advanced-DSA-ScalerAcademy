#
# Created on Thu Jun 23 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q2. Pairs with Given Difference

Problem Description
Given an one-dimensional integer array A of size N and an integer B.
Count all distinct pairs with difference equal to B.
Here a pair is defined as an integer pair (x, y), where x and y are both numbers in the array and their absolute difference is B.

Problem Constraints
1 <= N <= 104
0 <= A[i], B <= 105

Input Format
First argument is an one-dimensional integer array A of size N.

Second argument is an integer B.

Output Format
Return an integer denoting the count of all distinct pairs with difference equal to B.

Example Input
Input 1:
 A = [1, 5, 3, 4, 2]
 B = 3

Input 2:
 A = [8, 12, 16, 4, 0, 20]
 B = 4

Input 3:
 A = [1, 1, 1, 2, 2]
 B = 0

Example Output
Output 1:
 2

Output 2:
 5

Output 3:
 2

Example Explanation
Explanation 1:
 There are 2 unique pairs with difference 3, the pairs are {1, 4} and {5, 2} 

Explanation 2:
 There are 5 unique pairs with difference 4, the pairs are {0, 4}, {4, 8}, {8, 12}, {12, 16} and {16, 20} 

Explanation 3:
 There are 2 unique pairs with difference 0, the pairs are {1, 1} and {2, 2}.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return self.getPairsCountOfDifferenceK(A,B)

    def getPairsCountOfDifferenceK(self, input_array, k):
        #return the no.of pairs with the difference k
        pairCount = 0
        size = len(input_array)

        if size < 1:
            return pairCount

        elif size == 1:
            #Base constraint
            if input_array[0] == k:
                return 1
            else:
                return pairCount
        
        else:
            #Lets first sort the input array in descending order then we can apply 2-pointer approach
            #as we have to return a unique pair count lets maintain a hashmap
            hashmapPairs = dict()

            input_array.sort(reverse = True)
            p1 = 0
            p2 = 1            
            while p2 < size:
                #array is now sorted in descending order
                #per the constraints all the input array elements are >= 0 (positive)
                _diff = input_array[p1] - input_array[p2]
                if _diff == k:
                    if (input_array[p1],input_array[p2]) not in hashmapPairs:
                        pairCount += 1
                        hashmapPairs[(input_array[p1],input_array[p2])] = True
                    p2 += 1
                elif _diff < k:
                    #this means we are subtracting more value, so lets increment p2 to increase the diff., 
                    p2 += 1
                else:
                    #diff > k
                    p1 += 1
                    if p1 == p2:
                        p2 += 1
            
            return pairCount

s = Solution()
A = [1, 5, 3, 4, 2]
B = 3
ans = s.getPairsCountOfDifferenceK(A, B)
assert ans == 2

A = [8, 12, 16, 4, 0, 20]
B = 4
ans = s.getPairsCountOfDifferenceK(A, B)
assert ans == 5

A = [1, 1, 1, 2, 2]
B = 0
ans = s.getPairsCountOfDifferenceK(A, B)
assert ans == 2