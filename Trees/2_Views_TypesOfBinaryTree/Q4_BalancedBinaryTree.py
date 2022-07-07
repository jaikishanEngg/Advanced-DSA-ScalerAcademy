#
# Created on Thu Jul 07 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a root of binary tree A, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Problem Constraints
1 <= size of tree <= 100000

Input Format
First and only argument is the root of the tree A.

Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

Example Input
Input 1:

    1
   / \
  2   3

Input 2:

       1
      /
     2
    /
   3

Example Output
Output 1:
1

Output 2:
0

Example Explanation
Explanation 1:
    It is a complete binary tree.

Explanation 2:
    Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
    Difference = 2 > 1. 
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, rootNode):
        #first lets push all the nodes into a stack
        stack = []
        queue = []
        stack.append(rootNode)
        queue.append(rootNode)
        while(queue):
            currentNode = queue.pop(0) #deque front

            if currentNode.left:
                stack.append(currentNode.left)
                queue.append(currentNode.left)
            if currentNode.right:
                stack.append(currentNode.right)
                queue.append(currentNode.right)
        
        hashmapNodeLevel = dict()    #hashmap<Node, Level>

        while(stack):
            currentNode = stack.pop()
            if not currentNode.left and currentNode.right:
                #its a leaf node
                hashmapNodeLevel[currentNode.val] = 0
            if currentNode.left:
                left = 1 + hashmapNodeLevel[currentNode.left.val]
            else:
                left = 0
            if currentNode.right:
                right = 1 + hashmapNodeLevel[currentNode.right.val]
            else:
                right = 0
            
            balanceLevel = abs(left - right)
            if  balanceLevel > 1:
                #its not a balanced tree
                return 0
            else:
                hashmapNodeLevel[currentNode.val] = balanceLevel
        
        return 1

s = Solution()

'''
      1
     / \
    2   3

one = TreeNode(1)
one.left = TreeNode(2)
one.right = TreeNode(3)
'''

'''
        1
       /
      2
    /
   3
'''
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)

one.left = two
two.left = three

ans = s.isBalanced(one)
print(ans)


        
            


        
