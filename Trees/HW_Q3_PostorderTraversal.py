#
# Created on Mon Jul 04 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a binary tree, return the Postorder traversal of its nodes' values.
NOTE: Using recursion is not allowed.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.

Output Format
Return an integer array denoting the Postorder traversal of the given binary tree.

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
 [3, 2, 1]

Output 2:
 [6, 3, 2, 1]

Example Explanation
Explanation 1:
 The Preoder Traversal of the given tree is [3, 2, 1].

Explanation 2:
 The Preoder Traversal of the given tree is [6, 3, 2, 1].
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def postorderTraversal(self, rootNode):
        postorderTraversalList = []
        stack = []

        stack.append(rootNode) #initialize the stack with the rootNode

        while(stack):
            currentNode = stack.pop()
            postorderTraversalList.insert(0, currentNode.val)

            if currentNode.left:
                stack.append(currentNode.left)
            if currentNode.right:
                stack.append(currentNode.right)
            
        return postorderTraversalList
    
    def postorderTraversalWithRecursion(self, root):
        if root == None:
            return
        self.postorderTraversalWithRecursion(root.left)
        self.postorderTraversalWithRecursion(root.right)
        print(root.val, end = "  ")

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

s.postorderTraversalWithRecursion(rootNode)

ans = s.postorderTraversal(rootNode)
assert ans == [6,3,2,1]

