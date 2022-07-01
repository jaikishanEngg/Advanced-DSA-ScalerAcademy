#
# Created on Tue Jun 14 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Given a singly linked list, delete middle of the linked list.
For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5
If there are even nodes, then there would be two middle nodes, we need to delete the second middle element.
For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.
Return the head of the linked list after removing the middle node.
If the input linked list has 1 node, then this node should be deleted and a null node should be returned.

Input Format
The only argument given is the node pointing to the head node of the linked list
See Expected Output
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def removeMidElement(self, headPtr):
        cursorPtr = headPtr
        
        length = 0
        while(cursorPtr):
            length += 1
            cursorPtr = cursorPtr.next
        
        midElementInd = length//2 + 1
        
        if length <= 1:
            #If its a single element in the list, removing mid ele = removing itself. 
            return None

        #we need to hold a cursor at the previous element of the middle element in LL
        previousMidElement = midElementInd - 1

        cursorPtr = headPtr
        while(previousMidElement > 1):
            cursorPtr = cursorPtr.next
            previousMidElement -= 1
        
        if cursorPtr.next:
            if cursorPtr.next.next:
                cursorPtr.next = cursorPtr.next.next
            else:
                cursorPtr.next = None
        return headPtr

    def solve(self, headPtr):
        return self.removeMidElement(headPtr)











