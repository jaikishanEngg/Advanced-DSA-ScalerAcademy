#
# Created on Mon Jun 13 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You are given a singly linked list having head node A. You have to reverse the linked list and return the head node of that reversed list.

NOTE: You have to do it in-place and in one-pass.

Problem Constraints
1 <= Length of linked list <= 105
Value of each node is within the range of a 32-bit integer.

Input Format
First and only argument is a linked-list node A.

Output Format
Return a linked-list node denoting the head of the reversed linked list.

Example Input
Input 1:
    A = 1 -> 2 -> 3 -> 4 -> 5 -> NULL 

Input 2:
    A = 3 -> NULL 

Example Output
Output 1:
    5 -> 4 -> 3 -> 2 -> 1 -> NULL 

Output 2:
    3 -> NULL 

Example Explanation
Explanation 1:
    The linked list has 5 nodes. After reversing them, the list becomes : 5 -> 4 -> 3 -> 2 -> 1 -> NULL 

Expalantion 2:
    The linked list consists of only a single node. After reversing it, the list becomes : 3 -> NULL 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def reverseList(self, headPtr):
        if headPtr == None:
            return headPtr

        tempPtr = headPtr
        headPtr_2 = None
        while(headPtr):
            headPtr = headPtr.next
            tempPtr.next = headPtr_2
            headPtr_2 = tempPtr
            tempPtr = headPtr
        return headPtr_2



        

            


