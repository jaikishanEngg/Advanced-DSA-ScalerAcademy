#
# Created on Thu Jun 02 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You are given an integer array A having N integers.
You have to find the minimum length subarray A[l..r] such that sorting this subarray makes the whole array sorted.

Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109

Input Format
    First and only argument is an integer array A.

Output Format
    Return an integer denoting the minimum length.

Example Input
Input 1:
    A = [0, 1, 15, 25, 6, 7, 30, 40, 50] 

Input 2:
    A = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60] 

Example Output
Output 1:
    4 
Output 2:
    6 

Example Explanation
Explanation 1:
 The smallest subarray to be sorted to make the whole array sorted =  A[3..6] i.e, subarray lying between positions 3 and 6. 

Explanation 2:
 The smallest subarray to be sorted to make the whole array sorted =  A[4..9] i.e, subarray lying between positions 4 and 9. 
'''
class Solution:
    def bruteforceApproach(self, input_array):
        #This method takes input_array of size N and returns the smallest possible length of the sub-array
        # where by sorting the sub-array it makes the whole input_array sorted
        #In this approach we will sort the input array, and compare the elements
        # whenever we see a difference from starting it will be our start_index and from right-to-left first occurance
        # it will be end_index.  Length = end_index - start_index + 1

        sorted_input_array = sorted(input_array) #sorting will take O(N log N)
        start_index = None
        end_index = None

        for i in range(len(input_array)):
            if input_array[i] != sorted_input_array[i]:
                start_index = i
                break
        
        for j in range(len(input_array)-1, -1, -1):
            if input_array[j] != sorted_input_array[j]:
                end_index = j
                break

        return abs(end_index - start_index) + 1

    def smallestSubarrayLengthTobeSorted(self, input_array):
        #This method takes input_array of size N 
        # and returns the smallest possible length of the sub-array, by sorting it makes 
        # the whole input_array sorted
        
        #Approach: without sorting the array. Time = O(N)

        size = len(input_array)

        #find the mininum possible candidate which is violating the sorting order constraing, that is A[i-1] < A[i] (ascending order)
        _min = None
        for i in range(1, size):
            if input_array[i-1] > input_array[i]:
                if _min:
                    _min = min(_min, input_array[i])                    
                else:
                    _min = input_array[i]                    
        
        #find the maximum possible candidate which is violating the constraint, A[j] < A[j+1] (ascending order)
        _max = None
        for j in range(size-2, -1, -1):
            if input_array[j] > input_array[j+1]:
                if _max:
                    _max = max(_max, input_array[j])
                else:
                    _max = input_array[j]
        
        print("Minimum and maximum values violating sorting constraints: _min = {} and _max = {}".format(_min, _max))
        
        #if it is already a sorted array then _min or _max will be None;
        #so, we will check if _min or _max has some value then we will proceed finding the indexes for minimum and maximum value possible place
        if _min or _max:
            #Now find the index where _min and _max are violating
            min_index = None
            max_index = None

            for i in range(size):
                if input_array[i] > _min:
                    min_index = i
                    break

            for j in range(size-1, -1, -1):
                if input_array[j] < _max:
                    max_index = j
                    break
            
            print("min_index = {} max_index = {}".format(min_index, max_index))
            
            #return the length of the array, which needs to be sorted
            return abs(max_index - min_index) + 1
        
        else:
            #If the array is already in sorted ascending order return length as 0, which doesn't need to be sorted
            return 0

    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return self.smallestSubarrayLengthTobeSorted(A)

s = Solution()
input_array = [1,4,7,5,3,2,8,10,6,14,15]
#s.smallestSubarrayLengthTobeSorted(input_array)
input_array = [0, 1, 15, 25, 6, 7, 30, 40, 50] 
input_array = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
input_array = [ -146316343, 179840175, 760528516 ]
input_array = [ -999967396, -999888735, -999861273, -999347918, -998726759, -997399414, -859648220, -743113463, 692192828, 698431747, 985409072, 993282433, 997431107, 998481001, 999017658, 999886311, 999981981, 999990154, 999992820, 999995412, 999996444, 999998876, 999999929, 999999937, 999999958, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000 ]

#test case hard:
input_array = [ -999719982, -997706828, -997691325, -995251776, -990849335, -988481354, -981629779, -868737744, -120351267, 64788082, 228415163, 614611823, 640974381, -452682129, -965876048, 783056532, -453532535, 833834653, -987591077, 817673675, -544684968, -401051410, 132395537, 572296099, 353540327, -703539499, -766132674, 767205598, -279256033, 315415674, -152640056, -464821584, -167380503, -469901855, 559665312, 48354254, 170817182, -561161308, 83573785, 140331344, 737127606, 99308049, -43574593, 495163194, 595089965, -114946743, 616204212, 766575935, 967480596, 996730531, 998082304, 998152496, 998830044, 999684899, 999958768, 999995103, 999997947, 999998705, 999998949, 999999849, 999999855, 999999857, 999999974, 999999977, 999999999, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000 ]
assert s.solve(input_array) == 42
assert s.solve(input_array) == s.bruteforceApproach(input_array)
