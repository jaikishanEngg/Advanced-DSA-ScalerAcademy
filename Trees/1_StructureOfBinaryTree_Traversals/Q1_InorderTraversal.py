#
# Created on Sat Jul 02 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a binary tree, return the inorder traversal of its nodes' values.

NOTE: Using recursion is not allowed.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.

Output Format
Return an integer array denoting the inorder traversal of the given binary tree.

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

 [1, 3, 2]
Output 2:

 [6, 1, 3, 2]


Example Explanation
Explanation 1:

 The Inorder Traversal of the given tree is [1, 3, 2].
Explanation 2:

 The Inorder Traversal of the given tree is [6, 1, 3, 2].
'''
# Definition for a  binary tree node
from logging import root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
    def __init__(self):
        self.inorderList = []
        
    def inorderTraversal(self, root):
        if root == None:
            return
        
        self.inorderTraversal(root.left)
        self.inorderList.append(root.val)
        self.inorderTraversal(root.right)
        
        return self.inorderList

    def inorderTraversalWithoutRecursion(self, rootNode):
        #we use stack to keep a track of nodes we're visiting, instead of recursion
        stack = [] 
        inorderTraversal = [] #store inorder traversal result into a list variable

        currentNode = rootNode
        while(1):
            #scan through the left subtree as long as it is null, when it is null - then pop the element from the stack and add it to the ans, then traverse the right subtree
            if currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            elif stack:
                currentNode = stack.pop()
                inorderTraversal.append(currentNode.val)
                currentNode = currentNode.right
            else:
                break
        
        return inorderTraversal

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

ans = s.inorderTraversalWithoutRecursion(rootNode)
print(ans)
