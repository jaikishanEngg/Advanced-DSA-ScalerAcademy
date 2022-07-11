#
# Created on Sun Jul 10 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q3. Diameter of binary tree

Problem Description
Given a Binary Tree A consisting of N integer nodes, you need to find the diameter of the tree.
The diameter of a tree is the number of edges on the longest path between two nodes in the tree.

Problem Constraints
0 <= N <= 105

Input Format
First and only Argument represents the root of binary tree A.

Output Format
Return an single integer denoting the diameter of the tree.

Example Input
Input 1:
           1
         /   \
        2     3
       / \
      4   5

Input 2:
            1
          /   \
         2     3
        / \     \
       4   5     6

Example Output
Output 1:
     3

Output 2:
     4

Example Explanation
Explanation 1:
     Longest Path in the tree is 4 -> 2 -> 1 -> 3 and the number of edges in this path is 3 so diameter is 3.

Explanation 2:
     Longest Path in the tree is 4 -> 2 -> 1 -> 3 -> 6 and the number of edges in this path is 4 so diameter is 4.
'''
'''
Input 3:
                                        1
                                       /  \
                                      2     3
                                    /  \
                                   4    5
                                  /     /
                                 6     8
                                /     /
                               7     9
                              /
                             10
'''
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def computeDiameterandheightOfBinaryTree(self, node):
        if node == None:
            return -1
        leftHeight = self.computeDiameterandheightOfBinaryTree(node.left)
        rightHeight = self.computeDiameterandheightOfBinaryTree(node.right)
        self.diameter = max(self.diameter, 2 + leftHeight + rightHeight)
        return 1 + max(leftHeight, rightHeight)
        
    def diameterOfBinaryTree(self, rootNode):
        '''
        Diameter of the tree is max no.of edges between any two nodes
        For instance, in the input#1 above, the max. no.of edges possible between nodes 4 and 3 is = 3
        similarly, consider input #3 above, the max. no.of edges possible between nodes 10 and 9 is = 7
        '''
        self.diameter = -1 #initialize the diameter of binary tree to -1
        
        self.computeDiameterandheightOfBinaryTree(rootNode)

        return self.diameter

    def solve(self, rootNode):
        return self.diameterOfBinaryTree(rootNode)

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

s = Solution()
ans = s.solve(root)
assert ans == 5

'''
For example,
		 1
		/ \ 
       2   3
		  /
		 4
		 \
		  5
'''
one = TreeNode(1)
three = TreeNode(3)

one.left = TreeNode(2)
one.right = three

four = TreeNode(4)
three.left = four
four.right = TreeNode(5)

ans = s.solve(one)
assert ans == 4

'''
    3
   /
  26
'''
three = TreeNode(3)
three.left = TreeNode(26)

ans = s.solve(TreeNode(26))
assert ans == 0

'''
    3
   / \
  26  27
'''
three.right = TreeNode(27)
ans = s.solve(three)
assert ans == 2

'''
                                        1
                                       /  \
                                      2     3
                                    /  \
                                   4    5
                                  /     /
                                 6     8
                                /     /
                               7     9
                              /
                             10
'''
one = TreeNode(1);  two = TreeNode(2)
one.left = two; one.right = TreeNode(3)
four = TreeNode(4); five = TreeNode(5); six = TreeNode(6);  seven = TreeNode(7);    eight = TreeNode(8);    nine = TreeNode(9); ten = TreeNode(10)
two.left = four; two.right = five; four.left = six; five.left = eight; six.left = seven; eight.left = nine
seven.left = ten

ans = s.solve(one)
assert ans == 7
