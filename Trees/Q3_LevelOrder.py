#
# Created on Sun Jul 03 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q3. Level Order
Problem Description
Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Problem Constraints
1 <= number of nodes <= 105

Input Format
First and only argument is root node of the binary tree, A.

Output Format
Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.

Example Input
Input 1:

    3
   / \
  9  20
    /  \
   15   7

Input 2:

   1
  / \
 6   2
    /
   3

Example Output
Output 1:
 [
   [3],
   [9, 20],
   [15, 7]
 ]

Output 2:
 [ 
   [1]
   [6, 2]
   [3]
 ]

Example Explanation
Explanation 1:

 Return the 2D array. Each row denotes the traversal of each level.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.levelOrderTraversal = []
        self.queue = []
	
    # @param A : root node of tree
	# @return a list of list of integers
    def levelOrder(self, root):
        if root == None:
            return

        self.queue.append(root)

        while self.queue:
            elementsOfsamelevel = []
            level_size = len(self.queue)
            
            for i in range(level_size):
                currentNode = self.queue.pop(0) #dequeue the front node
                elementsOfsamelevel.append(currentNode.val)

                if currentNode.left:
                    self.queue.append(currentNode.left)
                if currentNode.right:
                    self.queue.append(currentNode.right)            
            
            self.levelOrderTraversal.append(elementsOfsamelevel)
        
        return self.levelOrderTraversal

'''
            3
          /   \
         9     20
       /  \    /  \
      1   2   13   7
     /   /
    4   5
The level order traversal of this tree should be --> [[3], [9, 20], [1, 2, 13, 7], [4, 5]]
'''
s = Solution()
root = TreeNode(3)
nine = TreeNode(9)
twenty = TreeNode(20)
root.left = nine
root.right = twenty
one = TreeNode(1)
nine.left = one
two = TreeNode(2)
nine.right = two
one.left = TreeNode(4)
two.left = TreeNode(5)

twenty.left = TreeNode(13)
twenty.right = TreeNode(7)

ans = s.levelOrder(root)
print(ans)
