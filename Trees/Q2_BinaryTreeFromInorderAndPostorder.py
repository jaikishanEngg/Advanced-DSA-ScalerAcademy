#
# Created on Sat Jul 02 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given the inorder and postorder traversal of a tree, construct the binary tree.

NOTE: You may assume that duplicates do not exist in the tree.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First argument is an integer array A denoting the inorder traversal of the tree.
Second argument is an integer array B denoting the postorder traversal of the tree.

Output Format
Return the root node of the binary tree.

Example Input
Input 1:
 A = [2, 1, 3]
 B = [2, 3, 1]

Input 2:
 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]

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
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
    
    def buildTreeFromInorderandPostorder(self, inorderList, postorderList, inorderStartIndex, inorderEndIndex, rootPositioninPostorder):
        #scan from postorderList in reverse to fetch the root node
        if inorderStartIndex > inorderEndIndex:
            return

        currentRootNode = TreeNode(postorderList[rootPositioninPostorder])

        inorderRootNodePosition = self.inorderDictionary[currentRootNode.val] #search for the rootNode position in the inorder list

        if inorderEndIndex == inorderStartIndex:
            return currentRootNode

        currentRootNode.right = self.buildTreeFromInorderandPostorder(inorderList, postorderList, inorderRootNodePosition+1,  inorderEndIndex, rootPositioninPostorder - 1)
        currentRootNode.left = self.buildTreeFromInorderandPostorder(inorderList, postorderList, inorderStartIndex, inorderRootNodePosition - 1, rootPositioninPostorder - (inorderEndIndex - inorderRootNodePosition) - 1)
        
        return currentRootNode

        
########################################
    def buildTree(self, inorderList, postorderList):
        totalNodes = len(postorderList)
        self.inorderDictionary = dict()
        for i in range(totalNodes):
            element = inorderList[i]
            if element not in self.inorderDictionary:
                self.inorderDictionary[element] = i
        return self.buildTreeFromInorderandPostorder(inorderList, postorderList, 0, len(inorderList)-1, rootPositioninPostorder = totalNodes-1)
    
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
        

#inorderList = [ 17, 12, 24, 13, 2, 22, 9, 20, 18, 23, 3, 15, 21, 10, 4, 11, 19, 14, 16, 7, 1, 5, 6, 8 ]
#postorderList = [ 17, 13, 2, 22, 24, 18, 20, 9, 15, 3, 11, 4, 10, 14, 16, 19, 1, 7, 21, 23, 12, 6, 8, 5 ]

#inorderList = [ 7, 5, 6, 2, 3, 1, 4 ]
#postorderList =  [ 5, 6, 3, 1, 4, 2, 7 ]
inorderList = [4,8,2,5,1,6,3,7]
postorderList = [8,4,5,2,6,7,3,1]

s = Solution()
_rootNode = s.buildTree(inorderList, postorderList)
print("pre-order traversal: ")
s.preorderTraversal(_rootNode)
print("\n************")
print("post-order traversal")
s.postorderTraversal(_rootNode)
print("\n************")
print("in-order traversal")
s.inorderTraversal(_rootNode)





        
        
