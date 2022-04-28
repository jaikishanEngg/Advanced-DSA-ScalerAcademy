#
# Created on Thu Apr 28 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next to each other.

Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, Given by the 2D array B

Problem Constraints
1 <= A <= 2 * 105
1 <= L <= R <= A
1 <= P <= 103
0 <= len(B) <= 105

Input Format
The first argument is a single integer A.
The second argument is a 2D integer array B.

Output Format
Return an array(0 based indexing) that stores the total number of coins in each beggars pot.

Example Input
Input 1:-
    A = 5
    B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

Example Output
    Output 1:-
    10 55 45 25 25

Example Explanation
Explanation 1:-
First devotee donated 10 coins to beggars ranging from 1 to 2. Final amount in each beggars pot after first devotee: [10, 10, 0, 0, 0]
Second devotee donated 20 coins to beggars ranging from 2 to 3. Final amount in each beggars pot after second devotee: [10, 30, 20, 0, 0]
Third devotee donated 25 coins to beggars ranging from 2 to 5. Final amount in each beggars pot after third devotee: [10, 55, 45, 25, 25]
'''
#Approach:
#A is the number of beggers
#B is the list of [start, end, contributed_amount] where it is 1-indexed
    #meaning from starting to ending devotee has contributed some amount to the beggers in lane
#We will first maintain the prefixSum array = [0] * num.of beggers
#We will traverse through list of lists in B:
    #[start, end, amount] we will add amount at the starting index in prefixSum and negation of the same amount after the end+1 index 
    #because only till the end amount we will consider it, after than we should not consider adding the amount after end index. so when we are doing prefix sum we should balance it, so we're adding negation at end+1 index 
#apply continuous sum on prefix sum array

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        numberofBeggers = A
        #B has [start, end, amount_donated]

        #initialize prefixSum array
        prefixSum = [0,]*numberofBeggers

        for l in B:
            #As these start and end are 1-index, remove 1 to match it with 0-index of our prefixSum array
            start = l[0] - 1
            end = l[1] - 1 

            amount = l[2]

            prefixSum[start] += amount
            if(end + 1 < numberofBeggers):
                prefixSum[end + 1] -= amount
        
        #compute prefixSum array
        for i in range(1, numberofBeggers):
            prefixSum[i] += prefixSum[i-1]
        
        return prefixSum

s = Solution()
numberofBeggers = 5
inputL = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
ans = s.solve(numberofBeggers, inputL)
print(ans)


