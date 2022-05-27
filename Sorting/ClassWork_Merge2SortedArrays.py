#
# Created on Wed May 25 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
class Solution:
    def merge(self, arr1, arr2):
        size1 = len(arr1)
        size2 = len(arr2)

        output = [] #this is the output array, merged arr1 and arr2

        #lets have two pointers pointing array1 and array2.
        a = 0
        b = 0

        while a != size1 and b != size2:
            if arr1[a] < arr2[b]:
                output.append(arr1[a])
                a += 1
            elif arr1[a] > arr2[b]:
                output.append(arr2[b])
                b += 1
            else:
                output.append(arr1[a])
                output.append(arr2[b])
                a += 1
                b += 1
        
        if a == size1:
            for ele in arr2[b:]:
                output.append(ele)
        elif b == size2:
            for ele in arr1[a:]:
                output.append(ele)
            
        return output

s = Solution()
A = [2, 5, 7, 12, 20, 24, 29]
B = [6, 9, 10, 14, 18, 19]
ans = s.merge(A, B)
print(ans)

A = [2, 4, 6]
B = [3, 5, 7]
ans = s.merge(A, B)

A = [ 1, 2 ]
B = [ -1, 2 ]
ans = s.merge(A, B)
print(ans)


