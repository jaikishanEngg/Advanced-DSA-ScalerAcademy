#
# Created on Mon Jul 04 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given preorder and inorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First argument is an integer array A denoting the preorder traversal of the tree.
Second argument is an integer array B denoting the inorder traversal of the tree.

Output Format
Return the root node of the binary tree.

Example Input
Input 1:
 A = [1, 2, 3]
 B = [2, 1, 3]

Input 2:
 A = [1, 6, 2, 3]
 B = [6, 1, 3, 2]

Example Output
Output 1:
   1
  / \
 2   3

Output 2:
   1  
  / \
 6   2
    /
   3

Example Explanation
Explanation 1:
 Create the binary tree and return the root node of the tree.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTreeFromInorderandPreorder(self, inorderList, preorderList, inorderStartIndex, inorderEndIndex, preorderRootIndex):
        if inorderStartIndex > inorderEndIndex:
            return
        rootElement = TreeNode(preorderList[preorderRootIndex])
        rootElementIndex = self.inorderDictionary[rootElement.val]

        rootElement.left = self.buildTreeFromInorderandPreorder(inorderList, preorderList, inorderStartIndex, rootElementIndex-1, preorderRootIndex+1)
        rootElement.right = self.buildTreeFromInorderandPreorder(inorderList, preorderList, rootElementIndex+1, inorderEndIndex, preorderRootIndex + (rootElementIndex - inorderStartIndex) + 1)

        return rootElement
    
    def buildTree(self, preorderList, inorderList):
        totalNodes = len(inorderList)
        self.inorderDictionary = dict() #maintain a hashmap to refer the rootIndex quickly
        for i in range(totalNodes):
            element = inorderList[i]
            if element not in self.inorderDictionary:
                self.inorderDictionary[element] = i
        return self.buildTreeFromInorderandPreorder(inorderList, preorderList, 0, totalNodes-1, 0)

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

preorderList = [1, 6, 2, 3]
inorderList = [6, 1, 3, 2]
s = Solution()
_rootNode = s.buildTree(preorderList, inorderList)
print("pre-order traversal: ")
s.preorderTraversal(_rootNode)
print("\n************")
print("post-order traversal")
s.postorderTraversal(_rootNode)
print("\n************")
print("in-order traversal")
s.inorderTraversal(_rootNode)


        
