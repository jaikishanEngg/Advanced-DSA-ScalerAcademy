#
# Created on Mon Jul 11 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Moris Inorder Traversal - Moris algorithm only works for Inorder traversal.
Previously we have solved Inorder traversal using 
    1. recursion - which takes O(N) stack space and O(N) time
    2. with out recursion - using stack where it takes O(N) space and O(n) time

but with Moris in-order traversal algorithm it takes just O(1) space while we have to scan through each node at least once, it takes O(N) time
'''
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None

class Solution:
    def morisInorderTraversal(self, rootNode):
        currentNode = rootNode
        while(currentNode):
            if not currentNode.left:
                print(currentNode.val, end = " ")
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
                    print(currentNode.val, end = " ")
                    currentNode = currentNode.right

'''
                        6
                         \
                          8
                           \
                           29
                         /    \
                        20     32
                      /  \    /   \
                    15   23  30    35
                   /  \    \
                  9   17    25
                   \    \
                    10   19
'''
six = TreeNode(6)
eight = TreeNode(8)
twenty_nine = TreeNode(29)
twenty = TreeNode(20)
thirty_two = TreeNode(32);  thirty = TreeNode(30);  thirty_five = TreeNode(35)
fifteen = TreeNode(15)
twenty_three = TreeNode(23);    twenty_five = TreeNode(25)
seventeen = TreeNode(17)
nine = TreeNode(9)
ten = TreeNode(10)
nineteen = TreeNode(19)

six.right = eight;  eight.right = twenty_nine
twenty_nine.left = twenty;  twenty_nine.right = thirty_two
twenty.left = fifteen;  twenty.right = twenty_three
thirty_two.left = thirty;   thirty_two.right = thirty_five
fifteen.left = nine;    fifteen.right = seventeen
twenty_three.right = twenty_five
nine.right = ten
seventeen.right = nineteen

s = Solution()
s.morisInorderTraversal(six)


                    
