#
# Created on Thu Jul 07 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a binary tree, return a 2-D array with vertical order traversal of it. Go through the example and image for more details.

NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.

Problem Constraints
0 <= number of nodes <= 105

Input Format
First and only arument is a pointer to the root node of binary tree, A.

Output Format
Return a 2D array denoting the vertical order traversal of tree as shown.

Example Input
Input 1:
      6
    /   \
   3     7
  / \     \
 2   5     9

Input 2:
      1
    /   \
   3     7
  /       \
 2         9

Example Output
Output 1:
 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]

Output 2:
 [
    [2],
    [3],
    [1],
    [7],
    [9]
 ]

Example Explanation
Explanation 1:
 First row represent the verical line 1 and so on.
'''
# Definition for a  binary tree node
from tkinter.tix import Tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
    def verticalOrderTraversal(self, rootNode):
        queue = []  #we will maintain a queue<(node, level)>
        hashMap = dict() #hashmap<Level, Node>

        queue.append((rootNode, 0))

        while(queue):
            currentItem = queue.pop(0)
            currentNode = currentItem[0]
            currentLevel = currentItem[1]

            if currentLevel in hashMap:
                hashMap[currentLevel].append(currentNode.val)
            else:
                hashMap[currentLevel] = [currentNode.val,]
            
            if currentNode.left:
                queue.append((currentNode.left, currentLevel - 1))
            if currentNode.right:
                queue.append((currentNode.right, currentLevel + 1))
        
        _minLevel = min(hashMap)
        _maxLevel = max(hashMap)

        verticalorderTraversalList = []
        for i in range(_minLevel, _maxLevel+1):
            verticalorderTraversalList.append(hashMap[i])
        
        return verticalorderTraversalList

s = Solution()

six = TreeNode(6)
three = TreeNode(3)
seven = TreeNode(7)

six.left = three
six.right = seven

three.left = TreeNode(2)
three.right = TreeNode(5)

seven.right = TreeNode(9)

ans = s.verticalOrderTraversal(six)
print(ans)
assert ans == [[2], [3], [6, 5], [7], [9]]




