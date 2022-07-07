#
# Created on Mon Jul 04 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a binary tree, return the preorder traversal of its nodes' values.
NOTE: Using recursion is not allowed.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.

Output Format
Return an integer array denoting the preorder traversal of the given binary tree.

Example Input
Input 1:

   1
    \
     2
    /
   3

Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:
 [1, 2, 3]

Output 2:
 [1, 6, 2, 3]

Example Explanation
Explanation 1:
 The Preoder Traversal of the given tree is [1, 2, 3].

Explanation 2:
 The Preoder Traversal of the given tree is [1, 6, 2, 3].
'''
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

class Solution:
   def preorderTraversal(self, rootNode):
      #preorder traversal without using recursion.
      stack = [] 
      preorderTraversal = [] #store preorder traversal result into a list variable

      currentNode = rootNode

      while(1):
         if currentNode:
            stack.append(currentNode)
            preorderTraversal.append(currentNode.val)
            currentNode = currentNode.left
         elif stack:
            currentNode = stack.pop()
            currentNode = currentNode.right
         else:
            break
      
      return preorderTraversal
      
   def preorderTraversal(self, root):
      if root == None:
         return
      print(root.val, end = "  ")
      self.preorderTraversal(root.left)
      self.preorderTraversal(root.right)
   
   def postorderTraversal(self, root):
      if root == None:
         return
      self.postorderTraversal(root.left)
      self.postorderTraversal(root.right)
      print(root.val, end = "  ")
   
   def inorderTraversal(self, root):
      if root == None:
         return
      self.inorderTraversal(root.left)
      print(root.val, end = "  ")
      self.inorderTraversal(root.right)        

s = Solution()

'''
   1
  / \
 6   2
    /
   3
'''
rootNode = TreeNode(1)     
rootNode.left = TreeNode(6)
two = TreeNode(2)    
rootNode.right = two
two.left = TreeNode(3)

ans = s.preorderTraversal(rootNode)
assert ans == [1, 6, 2, 3]
