#
# Created on Sun Jun 05 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given an array of N elements where all the elements occurs twice except one.  Find that unique element

Note: Duplicate elements occurs together.

One more observation -- no.of elements in array N = 2*k + 1 unique element; where all k elements occurs twice and 1 unique element.
Therefore N is odd
'''

from turtle import right


class Solution:
    def getUniqueElement(self, input_array, leftPtr, rightPtr):
        #Usually the first occurance of the duplicate element occurs at even index
        # unless it is disturbed by the unique element in between.
        if leftPtr == rightPtr:
            return input_array[leftPtr]

        while leftPtr <= rightPtr:
            midPtr = (leftPtr + rightPtr)//2
            midPtrType = midPtr % 2
            
            if input_array[midPtr] != input_array[midPtr - 1] and input_array[midPtr] != input_array[midPtr + 1]:
                return input_array[midPtr]
            
            elif midPtrType == 1:
                if input_array[midPtr-1] == input_array[midPtr]:
                    #first occurance is at even index, which is fine so lets check right
                    leftPtr = midPtr + 1
                else:
                    #first occurance is at odd index, then go left
                    rightPtr = midPtr - 1
                return self.getUniqueElement(input_array, leftPtr, rightPtr)
            
            else:
                #if the midptr is at even index
                if input_array[midPtr-1] == input_array[midPtr]:
                    #first occurance is at odd index, which is disturbed by unique element earlier, so lets check left
                    rightPtr = midPtr - 1
                else:
                    leftPtr = midPtr + 1
                
                return self.getUniqueElement(input_array, leftPtr, rightPtr)
        
        return None

    def solve(self, input_array):
        return self.getUniqueElement(input_array, 0, len(input_array)-1)

s = Solution()
input_array = [3,3,1,1,8,2,2]
assert s.solve(input_array) == 8

input_array = [1,2,2]
assert s.solve(input_array) == 1

input_array = [2,2,5]
assert s.solve(input_array) == 5
        
input_array = [0,0,5,1,1]
assert s.solve(input_array) == 5


