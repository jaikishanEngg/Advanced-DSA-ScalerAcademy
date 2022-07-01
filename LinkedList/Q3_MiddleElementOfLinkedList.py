#
# Created on Tue Jun 14 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q3. Middle element of linked list
Problem Description
Given a linked list of integers, find and return the middle element of the linked list.

NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.

Problem Constraints
1 <= length of the linked list <= 100000
1 <= Node value <= 109

Input Format
The only argument given head pointer of linked list.

Output Format
Return the middle element of the linked list.

Example Input
Input 1:
    1 -> 2 -> 3 -> 4 -> 5

Input 2:
    1 -> 5 -> 6 -> 2 -> 3 -> 4

Example Output
Output 1:
    3

Output 2:
    2

Example Explanation
Explanation 1:
    The middle element is 3.

Explanation 2:
    The middle element in even length linked list of length N is ((N/2) + 1)th element which is 2.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer    
    def getMiddleElementOfTheList(self, headPtr):
        cursorPtr = headPtr
        length = 0
        while(cursorPtr):
            length += 1
            cursorPtr = cursorPtr.next
        
        middlePtrIndex = (length//2 ) + 1

        cursorPtr = headPtr
        middlePtrIndex -= 1
        while(cursorPtr and middlePtrIndex):
            cursorPtr = cursorPtr.next
            middlePtrIndex -= 1
        
        return cursorPtr.val
    
    def solve(self, headPtr):
        return self.getMiddleElementOfTheList(headPtr)
    
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
#node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
#node5.next = node6

print("Original Linked List")
s.printList(node1)
print(s.solve(node1))

