#
# Created on Sat Jul 09 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q2. Least Common Ancestor

Problem Description
Find the lowest common ancestor in an unordered binary tree A, given two values, B and C, in the tree.
Lowest common ancestor: the lowest common ancestor (LCA) of two nodes, v and w in a tree or directed acyclic graph (DAG) is the lowest (i.e., deepest) node that has both v and w as descendants.

Problem Constraints
1 <= size of tree <= 100000
1 <= B, C <= 109

Input Format
First argument is head of tree A.
Second argument is integer B.
Third argument is integer C.

Output Format
Return the LCA.

Example Input
Input 1:
      1
     /  \
    2    3
B = 2
C = 3

Input 2:
      1
     /  \
    2    3
   / \
  4   5
B = 4
C = 5

Example Output
Output 1:
     1

Output 2:
     2

Example Explanation
Explanation 1:
 LCA is 1.

Explanation 2:
 LCA is 2.
'''
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    def pathFromRootToNodeWithDirection(self, root, nodeVal):
        path = []
        #return the path from root to the node with direction (text)
        if root == None:
            return 
        if root.val == nodeVal:
            return root.val
        
        _left = self.pathFromRootToNode(root.left, nodeVal)
        _right = self.pathFromRootToNode(root.right, nodeVal)
        
        if _left or _right:
            if _left:
                path.append(root.val)
                path.append("Left")
                path.append(_left)
                return path
            else:
                path.append(root.val)
                path.append("Right")
                path.append(_right)
                return path
        
        return path

    def pathFromRootToNode(self, root, nodeVal):
        path = []

        if root == None:
            return
        
        if root.val == nodeVal:
            return [root.val,]
        
        _left = self.pathFromRootToNode(root.left, nodeVal)
        _right = self.pathFromRootToNode(root.right, nodeVal)

        if _left or _right:
            path.extend([root.val])
            if _left:
                path.extend(_left)
                return path
            if _right:
                path.extend(_right)
                return path
        
        return path

    def lca(self, rootNode, node1Val, node2Val):
        #we have to return the least common ancestor of node1 and node2
        #Approach1:  find the path of node1 and node2 from root seperately.  Last common node in the path is the LCA. 
        #   and if we cancel the common part, the remaining nodes will give the path from node1 to node2
        pathforNode1 = self.pathFromRootToNode(rootNode, node1Val)
        pathforNode2 = self.pathFromRootToNode(rootNode, node2Val)

        if not pathforNode1 or not pathforNode2:
            return -1

        temp_length = min(len(pathforNode1), len(pathforNode2))
        for i in range(temp_length):
            if pathforNode1[i] == pathforNode2[i]:
                if i+1 >= temp_length or pathforNode1[i+1] != pathforNode2[i+1]:
                    return pathforNode1[i]

s = Solution()

'''
            3
          /   \
         9     20
       /  \    /  \
      1   2   13   7
     /   /
    4   5
'''
root = TreeNode(3)
nine = TreeNode(9)
twenty = TreeNode(20)
root.left = nine;   root.right = twenty
one = TreeNode(1)
two = TreeNode(2)
nine.left = one;    nine.right = two
one.left = TreeNode(4)
two.left = TreeNode(5)

twenty.left = TreeNode(13); twenty.right = TreeNode(7)

ans = s.pathFromRootToNode(root, 2)
assert ans == [3, 9, 2]
        
ans = s.pathFromRootToNode(root, 33)
print(ans)

LCA = s.lca(root, 2, 9)
assert LCA == 9

LCA = s.lca(root, 4, 5)
assert LCA == 9

LCA = s.lca(root, 13, 5)
assert LCA == 3

LCA = s.lca(root, 2, 7)
assert LCA == 3