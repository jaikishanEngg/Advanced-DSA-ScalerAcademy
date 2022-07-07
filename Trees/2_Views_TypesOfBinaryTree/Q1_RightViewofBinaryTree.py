#
# Created on Tue Jul 05 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
            3
          /   \
         9     20
       /  \    /  \
      1   2   13   7
     /   /
    4   5
The level order traversal of this tree looks like  --> 
[[3, None],
[9, 20, None],
[1, 2, 13, 7, None],
[4, 5, None]]

We have to print the nodes of right view of the tree. that is only the nodes [3, 20, 7, 5]
So, if we observe the level order then we have to consider just the previous element of None in the each level order.
'''
# Definition for a  binary tree node
from turtle import right


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def rightview(self, rootNode):
        queue = []
        rightviewList = []

        queue.append(rootNode) 
        #rightviewList.append(rootNode.val) #rightviewList.append(rootNode.val) #as the root node is always in the right view, lets add it

        while(queue):
            l = len(queue)
            for i in range(l):
                currentNode = queue.pop(0) #deque the front node of the queue
                if i == l - 1:
                    rightviewList.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)

        return rightviewList

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

s = Solution()
ans = s.rightview(root)
print(ans)
assert ans == [3, 20, 7, 5]