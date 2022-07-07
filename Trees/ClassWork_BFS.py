#
# Created on Tue Jul 05 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def BFS(self, rootNode):
        queue = []
        queue.append(rootNode)
        bfs = []
        while(queue):
            currentNode = queue.pop(0) #deque the front node of the queue
            bfs.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return bfs

'''
            3
          /   \
         9     20
       /  \    /  \
      1   2   13   7
     /   /
    4   5
The level order traversal of this tree should be --> [3, 9, 20, 1, 2, 13, 7, 4, 5]
'''
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
ans = s.BFS(root)
print(ans)