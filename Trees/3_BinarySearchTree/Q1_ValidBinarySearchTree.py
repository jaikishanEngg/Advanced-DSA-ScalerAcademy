#
# Created on Thu Jul 07 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q1. Valid Binary Search Tree

Problem Description
You are given a binary tree represented by root A.
Assume a BST is defined as follows:
1) The left subtree of a node contains only nodes with keys less than the node's key.
2) The right subtree of a node contains only nodes with keys greater than the node's key.
3) Both the left and right subtrees must also be binary search trees.

Problem Constraints
1 <= Number of nodes in binary tree <= 105
0 <= node values <= 109

Input Format
First and only argument is head of the binary tree A.

Output Format
Return 0 if false and 1 if true.

Example Input
Input 1:

   1
  /  \
 2    3

Input 2:

  2
 / \
1   3

Example Output

Output 1:
 0

Output 2:
 1

Example Explanation

Explanation 1:
 2 is not less than 1 but is in left subtree of 1.

Explanation 2:
Satisfies all conditions.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def isValidBinarySearchTree(self, rootNode, minValue, maxValue):
        if rootNode == None:
            return True
        if rootNode.val >= minValue and rootNode.val <= maxValue:
            return self.isValidBinarySearchTree(rootNode.left, minValue, rootNode.val - 1) and self.isValidBinarySearchTree(rootNode.right, rootNode.val+1, maxValue)
        else:
            return False

    def isValidBST(self, rootNode):
        if self.isValidBinarySearchTree(rootNode, float('-inf'), float('inf')):
            return 1
        else:
            return 0


s = Solution()

'''
Input 1:
 
   1
  /  \
 2    3

one = TreeNode(1)
one.left = TreeNode(2)
one.right = TreeNode(3)

ans = s.isValidBST(one)
print(ans)
assert ans == 0

Input 2:
 
  2
 / \
1   3
'''
one = TreeNode(1)
one.left = TreeNode(2)
one.right = TreeNode(3)

ans = s.isValidBST(one)
print(ans)
assert ans == 0

two = TreeNode(2)
two.left = TreeNode(1)
two.right = TreeNode(3)

ans = s.isValidBST(two)
print(ans)
#assert ans == 0


