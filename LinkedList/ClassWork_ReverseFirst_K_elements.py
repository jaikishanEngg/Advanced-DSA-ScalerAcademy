#
# Created on Mon Jun 13 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, value):
       self.val = value
       self.next = None

class Solution:
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

	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def reverseList(self, headPtr, k):
        '''
        This method reverses the first k elements and returns the headPtr
        '''
        if headPtr == None or k <= 1:
            return headPtr
        
        return self.reverseBetween(headPtr, 1, k)

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

k = 3
ptr = s.reverseList(node1, k)
print("After reversing the first {} element of the list ".format(k))
s.printList(ptr)
