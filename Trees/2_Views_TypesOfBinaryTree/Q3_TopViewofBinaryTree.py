#
# Created on Thu Jul 07 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q3. Top View of Binary tree

Problem Description
Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.
The top view of a Binary Tree is a set of nodes visible when the tree is visited from the top.
Return the nodes in any order.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Input Format
First and only argument is head of the binary tree A.

Output Format
Return an array, representing the top view of the binary tree.

Example Input
Input 1:

            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 

Input 2:

            1
           /  \
          2    3
           \
            4
             \
              5

Example Output
Output 1:
     [1, 2, 4, 8, 3, 7]

Output 2:
     [1, 2, 3]

Example Explanation
Explanation 1:
    Top view is described.

Explanation 2:
    Top view is described.
'''
# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def topviewofBinaryTree(self, rootNode):
        if rootNode == None:
            return
        
        queue = []
        #lets add the root node into the queue with #level
        queue.append((rootNode,0))
        hashMap = dict() #lets create a hashmap<level, Node>

        while(queue):
            currentElement = queue.pop(0) #deque the front element from the queue
            currentNode = currentElement[0]
            currentLevel = currentElement[1]

            if currentLevel not in hashMap:
                hashMap[currentLevel] = currentNode.val
            
            if currentNode.left:
                queue.append((currentNode.left, currentLevel - 1))
            if currentNode.right:
                queue.append((currentNode.right, currentLevel + 1))
            
        _minLevel = min(hashMap)
        _maxLevel = max(hashMap)
        topviewofBinaryTreeList = []
        for i in range(0, _minLevel-1, -1):
            topviewofBinaryTreeList.append(hashMap[i])
        
        for i in range(1, _maxLevel+1):
            topviewofBinaryTreeList.append(hashMap[i])

        return topviewofBinaryTreeList

    def solve(self, rootNode):
        return self.topviewofBinaryTree(rootNode)

s = Solution()
'''
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
'''

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)

one.left = two
one.right = three

two.left = four
two.right = TreeNode(5)

three.left = TreeNode(6)
three.right = TreeNode(7)

four.left = TreeNode(8)

ans = s.solve(one)
print(ans)
assert ans == [1, 2, 4, 8, 3, 7]