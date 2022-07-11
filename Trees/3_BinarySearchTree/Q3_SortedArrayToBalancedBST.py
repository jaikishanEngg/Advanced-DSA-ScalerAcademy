#
# Created on Fri Jul 08 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q3. Sorted Array To Balanced BST

Problem Description
Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).
Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Problem Constraints
1 <= length of array <= 100000

Input Format
First argument is an integer array A.

Output Format
Return a root node of the Binary Search Tree.

Example Input
Input 1:
 A : [1, 2, 3]

Input 2:
 A : [1, 2, 3, 5, 10]

Example Output
Output 1:
      2
    /   \
   1     3

Output 2:
      3
    /   \
   2     5
  /       \
 1         10

Example Explanation
Explanation 1:
    You need to return the root node of the Binary Tree.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def toBST(self, sortedList, startIndex, endIndex):
        if startIndex > endIndex:
            return

        mid = (endIndex + startIndex) // 2
        rootNodeElement = sortedList[mid]
        rootNode = TreeNode(rootNodeElement)
        
        #for LST
        rootNode.left = self.toBST(sortedList, startIndex, mid - 1)
        rootNode.right = self.toBST(sortedList, mid + 1, endIndex)
           
        return rootNode

    def sortedArrayToBST(self, sortedList):
        return self.toBST(sortedList, 0, len(sortedList)-1)
    
    def inorderTraversal(self, root):
        if root == None:
            return
        self.inorderTraversal(root.left)
        print(root.val, end = "  ")
        self.inorderTraversal(root.right)
    
    def preorderTraversal(self, root):
        if root == None:
            return
        print(root.val, end = "  ")
        self.inorderTraversal(root.left)
        self.inorderTraversal(root.right)

s = Solution()
'''
      3
    /   \
   2     5
  /       \
 1         10
'''
three = TreeNode(3)
two = TreeNode(2)
five = TreeNode(5)

three.left = two
three.right = five
two.left = TreeNode(1)
five.right = TreeNode(10)

ansRootNode = s.sortedArrayToBST([1, 2, 3, 5, 10])
s.inorderTraversal(ansRootNode)
print("\n***********")
print("Pre-order traversal")
s.preorderTraversal(ansRootNode)