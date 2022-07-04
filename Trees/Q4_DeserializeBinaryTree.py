#
# Created on Mon Jul 04 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
You are given an integer array A denoting the Level Order Traversal of the Binary Tree.
You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.

NOTE:
In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.

Problem Constraints
1 <= number of nodes <= 105
-1 <= A[i] <= 105

Input Format
Only argument is an integer array A denoting the Level Order Traversal of the Binary Tree.

Output Format
Return the root node of the Binary Tree.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]

Input 2:
 A = [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]

Example Output
Output 1:
           1
         /   \
        2     3
       / \
      4   5

Output 2:
            1
          /   \
         2     3
        / \ .   \
       4   5 .   6

Example Explanation

Explanation 1:
 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3, 4 and 5 each has both NULL child we had represented that using -1.

Explanation 2:
 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3 has left child as NULL while 4 and 5 each has both NULL child.
'''
import sys

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deserializeBinaryTree(self, levelorderList):
        queue = []
        rootNode = TreeNode(levelorderList[0])
        queue.append(rootNode)
        
        for i in range(1, len(levelorderList), 2):
            currentNode = queue.pop(0) #dequeue the front Node from the queue

            leftElement = levelorderList[i]
            rightElement = levelorderList[i + 1]

            if leftElement != -1:
                currentNode.left = TreeNode(leftElement)
                queue.append(currentNode.left)
            if rightElement != -1:
                currentNode.right = TreeNode(rightElement)
                queue.append(currentNode.right)

        return rootNode

    def solve(self, levelorderList):
        n = len(levelorderList)
        sys.setrecursionlimit(n + 4) #reset the recursion depth
        return self.deserializeBinaryTree(levelorderList)
    
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
levelorderList = [1,2,3,4,5, -1,-1, -1,-1, -1,-1]
root = s.solve(levelorderList)

s.preorderTraversal(root)