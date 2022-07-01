#
# Created on Tue Jun 28 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Return N-th number (use 1,2,3 digits) in the sequence
The sequence looks like 1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 32, 33, 111, 112, 113, 121, 122, 123, 131, 132, 133, ...
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
            print("Queu underflow!")
    
    def frontPtr(self):
        return self.front_ptr.value

class SequenceSolution:
    def __init__(self):
        pass
        
    def getNthNumber(self, n):
        seq_queue = Queue()
        seq_queue.enque(1)
        seq_queue.enque(2)
        seq_queue.enque(3)

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
            seq_queue.enque(x*10 + 3)
            counter += 1
        
        while counter < n:
            seq_queue.deque()
            counter += 1
        
        ans = seq_queue.front_ptr.value
        #self.seq_queue.front_ptr = self.queue_front_ptr
        return ans

s = SequenceSolution()
ans = s.getNthNumber(1)
assert ans == 1

ans = s.getNthNumber(3)
assert ans == 3

ans = s.getNthNumber(4)
assert ans == 11

ans = s.getNthNumber(10)
assert ans == 31

ans = s.getNthNumber(39)
print(ans)




