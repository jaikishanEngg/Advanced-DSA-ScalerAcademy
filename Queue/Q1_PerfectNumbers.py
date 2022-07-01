#
# Created on Wed Jun 29 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Q1. Perfect Numbers

Problem Description
Given an integer A, you have to find the Ath Perfect Number.
A Perfect Number has the following properties:
It comprises only 1 and 2.
The number of digits in a Perfect number is even.
It is a palindrome number.

For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.

Problem Constraints
1 <= A <= 100000


Input Format
The only argument given is an integer A.

Output Format
Return a string that denotes the Ath Perfect Number.

Example Input
Input 1:
 A = 2

Input 2:
 A = 3

Example Output
Output 1:
 22

Output 2:
 1111

Example Explanation
Explanation 1:
First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221

Explanation 2:
First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
'''
class Node:
    def __init__(self, data):
        self.value = data
        self.next_ptr = None

class Queue:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None
        self.size = 0
    
    def enque(self, item):
        new_item = Node(item)
        if self.rear_ptr == None:
            self.front_ptr = new_item
            self.rear_ptr = new_item
        else:
            self.rear_ptr.next_ptr = new_item
            self.rear_ptr = new_item
        self.size += 1

    def deque(self):
        if self.size > 0:
            cursor = self.front_ptr
            self.front_ptr = cursor.next_ptr
            self.size -= 1
        else:
            print("Queue underflow!")
    
    def frontPtr(self):
        return self.front_ptr.value


class Solution:
    def getNthNumber(self, n):
        seq_queue = Queue()
        seq_queue.enque(1)
        seq_queue.enque(2)
        
        #return the N-th number from the sequence
        nthNumber = None
        if n < 1:
            return nthNumber

        counter = 1
        while(seq_queue.size < n):
            #we build the sequence till the nearest N
            x = seq_queue.frontPtr()
            seq_queue.deque()
            seq_queue.enque(x*10 + 1)
            seq_queue.enque(x*10 + 2)
            counter += 1
        
        while counter < n:
            seq_queue.deque()
            counter += 1
        
        ans = seq_queue.front_ptr.value
        #self.seq_queue.front_ptr = self.queue_front_ptr
        return ans

    # @param A : integer
    # @return a strings
    def solve(self, n):
        x = str(self.getNthNumber(n))
        y = x[::-1]
        return x+y

s = Solution()
for i in range(1,11):
    print(s.solve(i))
