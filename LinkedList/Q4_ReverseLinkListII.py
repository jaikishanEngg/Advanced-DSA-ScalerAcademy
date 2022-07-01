#
# Created on Mon Jun 13 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Reverse a linked list A from position B to C.

NOTE: Do it in-place and in one-pass.

Problem Constraints
1 <= |A| <= 106
1 <= B <= C <= |A|

Input Format
The first argument contains a pointer to the head of the given linked list, A.
The second arugment contains an integer, B.
The third argument contains an integer C.

Output Format
    Return a pointer to the head of the modified linked list.

Example Input
Input 1:
    A = 1 -> 2 -> 3 -> 4 -> 5
    B = 2
    C = 4

Input 2:
    A = 1 -> 2 -> 3 -> 4 -> 5
    B = 1
    C = 5

Example Output
Output 1:
    1 -> 4 -> 3 -> 2 -> 5

Output 2:
    5 -> 4 -> 3 -> 2 -> 1

Example Explanation
Explanation 1:

 In the first example, we want to reverse the highlighted part of the given linked list : 1 -> 2 -> 3 -> 4 -> 5 
 Thus, the output is 1 -> 4 -> 3 -> 2 -> 5 

Explanation 2:

 In the second example, we want to reverse the highlighted part of the given linked list : 1 -> 4 -> 3 -> 2 -> 5  
 Thus, the output is 5 -> 4 -> 3 -> 2 -> 1 
'''
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
    def reverseBetween(self, headPtr, start, end):
        '''
        This method reverses the singly linked list between the start and end positions; 
        # returns the head pointer
        # 1 <= start <= end <= |A|
        '''
        if headPtr == None or start >= end or end <= 1:
            return headPtr
        
        cursorPtr = headPtr
        currentPosition = 1
        if start > 1:
            while(currentPosition < start-1):
                cursorPtr = cursorPtr.next
                currentPosition += 1
            
            preHeadPtr = cursorPtr
            cursorPtr = cursorPtr.next
            currentPosition += 1

        tempPtr = cursorPtr
        reverseHeadPtr = None
        while(cursorPtr and currentPosition <= end):
            cursorPtr = cursorPtr.next
            tempPtr.next = reverseHeadPtr
            reverseHeadPtr = tempPtr
            tempPtr = cursorPtr
            currentPosition += 1
        
        if start == 1:
            headPtr.next = cursorPtr
            headPtr = reverseHeadPtr
        else:
            preHeadPtr.next.next = cursorPtr
            preHeadPtr.next = reverseHeadPtr
        
        return headPtr

    def printList(self, headPtr):
        cursorPtr = headPtr

        while(cursorPtr):
            print(cursorPtr.val, end= " -> ")
            cursorPtr = cursorPtr.next
        print("None")


s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original Linked List")
s.printList(node1)

start = 2; end = 5
ptr = s.reverseBetween(node1, start, end)
print("After reversing the list from {} to {}".format(start, end))
s.printList(ptr)



        
