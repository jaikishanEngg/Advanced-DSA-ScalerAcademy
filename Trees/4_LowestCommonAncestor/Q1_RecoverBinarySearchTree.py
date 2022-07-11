#
# Created on Mon Jul 11 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q1. Recover Binary Search Tree

Problem Description
Two elements of a binary search tree (BST), represented by root A are swapped by mistake. Tell us the 2 values swapping which the tree will be restored.
A solution using O(n) space is pretty straightforward. Could you devise a constant space solution?

Problem Constraints
1 <= size of tree <= 100000

Input Format
First and only argument is the head of the tree,A

Output Format
Return the 2 elements which need to be swapped.

Example Input
Input 1:
         1
        / \
       2   3

Input 2:
         2
        / \
       3   1

Example Output
Output 1:
     [2, 1]

Output 2:
     [3, 1]

Example Explanation
Explanation 1:
    Swapping 1 and 2 will change the BST to be 
         2
        / \
       1   3
which is a valid BST 

Explanation 2:
    Swapping 1 and 3 will change the BST to be 
         2
        / \
       1   3
which is a valid BST 
'''
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    def morisInorderTraversal(self, rootNode):
        currentNode = rootNode
        firstVal = -1
        midVal = -1
        lastVal = -1

        previousNode = None
        #we will check for inversions when there is no left child/sub-tree
        while(currentNode):
            if not currentNode.left:
                if not previousNode:
                    #first node, so don't need to compare it with anything
                    previousNode = currentNode
                    currentNode = currentNode.right
                else:
                    #compare previousNode and currentNode
                    if currentNode.val < previousNode.val:
                        #Inversions
                        if firstVal == -1:
                            firstVal = previousNode
                            midVal = currentNode
                        else:
                            lastVal = currentNode
                    previousNode = currentNode
                    currentNode = currentNode.right
            
            elif currentNode.left:
                temp = currentNode.left
                while(temp.right and temp.right != currentNode):
                    temp = temp.right
                if temp.right == None:
                    temp.right = currentNode
                    currentNode = currentNode.left
                elif temp.right == currentNode:
                    temp.right = None
                    #compare previousNode and currentNode
                    if currentNode.val < previousNode.val:
                        #Inversions
                        if firstVal == -1:
                            firstVal = previousNode
                            midVal = currentNode
                        else:
                            lastVal = currentNode
                    previousNode = currentNode
                    currentNode = currentNode.right
        if firstVal == -1:
            print("No inversions.  The tree is a perfect BST!")
        
        #But per the question, there will be two nodes swapped and we need to return them.
        else:
            if lastVal == -1:
                #only one inversion occured
                #print("first value: ", firstVal.val, "middle value: ", midVal.val)
                return [firstVal.val, midVal.val]
            else:
                #two inversions
                #print("first value: ", firstVal.val, "last value:", lastVal.val)
                return [firstVal.val, lastVal.val]
    
    def recoverTree(self, rootNode):
        return sorted(self.morisInorderTraversal(rootNode))

'''
             5
           /  \ 
          3     8 
         / \   / \
        1  10  7  4 
'''
five = TreeNode(5)
three = TreeNode(3)
eight = TreeNode(8)

five.left = three; five.right = eight
three.left = TreeNode(1)
three.right = TreeNode(10)
eight.left = TreeNode(7)
eight.right = TreeNode(4)

s = Solution()
ans = s.recoverTree(five)
print(ans)