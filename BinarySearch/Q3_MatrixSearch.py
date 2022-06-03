#
# Created on Fri Jun 03 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A.
This matrix A has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

NOTE: Rows are numbered from top to bottom, and columns are from left to right.

Problem Constraints
1 <= N, M <= 1000
1 <= A[i][j], B <= 106

Input Format
    The first argument given is the integer matrix A.
    The second argument given is the integer B.

Output Format
    Return 1 if B is present in A else, return 0.

Example Input
Input 1:
A = [ 
      [1,   3,  5,  7]
      [10, 11, 16, 20]
      [23, 30, 34, 50]  
    ]
B = 3

Input 2:
A = [   
      [5, 17, 100, 111]
      [119, 120, 127, 131]    
    ]
B = 3

Example Output
Output 1:
    1
Output 2:
    0

Example Explanation
Explanation 1:
    3 is present in the matrix at A[0][1] position so return 1.
Explanation 2:
    3 is not present in the matrix so return 0.
'''
class Solution:
    def getRowIndexOfElement(self, input_matrix, colPtr, startPtr, endPtr, target):
        #returns the rowID where the target can be found, by only looking at the last column elements.
        #As the elements are sorted.
        while startPtr <= endPtr:
            mid = (startPtr + endPtr)//2
            if input_matrix[mid][colPtr] == target:
                return mid
            elif target < input_matrix[mid][colPtr]:
                endPtr = mid - 1
                return self.getRowIndexOfElement(input_matrix, colPtr, startPtr, endPtr, target)
            else:
                startPtr = mid + 1
                return self.getRowIndexOfElement(input_matrix, colPtr, startPtr, endPtr, target)
        
        return endPtr + 1
    
    def binarySearch(self, input_matrix, rowPtr, startPtr, endPtr, target):
        #as we got the tentative row where the target can be present, apply binary search on that row 
        #for the target, if found return True/1 else return False/0
        while startPtr <= endPtr:
            mid = (startPtr + endPtr)//2
            if input_matrix[rowPtr][mid] == target:
                return 1
            elif target > input_matrix[rowPtr][mid]:
                startPtr = mid + 1
                return self.binarySearch(input_matrix, rowPtr, startPtr, endPtr, target)
            else:
                endPtr = mid - 1
                return self.binarySearch(input_matrix, rowPtr, startPtr, endPtr, target)
        return 0

    # @param A : list of list of integers    # @param B : integer    # @return an integer
    def searchMatrix(self, input_matrix, search_element):
        rows = len(input_matrix)
        cols = len(input_matrix[0])

        #as the matrix is sorted.
        # A = [ [1,   3,  5,  7]
        #       [10, 11, 16, 20]
        #       [23, 30, 34, 50]  ]  search_element = 11
        # I'll start searching the last column, apply binary search, 11 can fall between 7 and 20. so I'll search row 1

        colPtr = cols - 1
        rowPtr = rows - 1
        get_row_index = self.getRowIndexOfElement(input_matrix, colPtr, 0, rows - 1, search_element)

        #now apply binary search and find the target element in that row ID (get_row_index) only
        if get_row_index >= 0 and get_row_index <= rows-1:
            return self.binarySearch(input_matrix, get_row_index, 0, cols -1, search_element)
        else:
            return 0


s = Solution()

A = [   
      [5, 17, 100, 111],
      [119, 120, 127, 131],
    ]
search_element = 3
A =[
  [1, 1, 2, 2, 5, 6, 6, 6, 7],
  [9, 10, 10, 12, 12, 13, 14, 21, 21],
  [23, 26, 26, 29, 29, 31, 32, 35, 37],
  [38, 39, 39, 39, 41, 41, 42, 42, 43],
  [45, 45, 46, 46, 46, 47, 48, 48, 51],
  [51, 51, 54, 54, 54, 54, 56, 58, 59],
  [60, 61, 61, 62, 63, 64, 65, 66, 67],
  [67, 67, 70, 70, 71, 73, 73, 73, 74],
  [74, 79, 79, 80, 82, 84, 84, 84, 87],
  [89, 93, 94, 94, 97, 98, 98, 98, 98],
]
search_element = 64
assert s.searchMatrix(A, search_element) == 1
A = [ 
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50], 
    ]
search_element = 55
assert s.searchMatrix(A, search_element) == 0
A =[
  [1, 4, 5, 5, 6, 14, 14, 16, 19],
  [22, 24, 28, 33, 35, 37, 38, 40, 41],
  [45, 50, 52, 55, 56, 56, 57, 60, 60],
  [63, 64, 66, 68, 68, 71, 78, 78, 79],
  [84, 89, 90, 91, 93, 94, 94, 97, 98],
]
search_element = 68
assert s.searchMatrix(A, search_element) == 1

A = [
    [22, 32, 67],
    ]
search_element = 93
assert s.searchMatrix(A, search_element) == 0
A = [
  [3, 4, 9, 10, 14, 17, 18, 20, 29, 32],
  [33, 36, 38, 46, 51, 52, 56, 56, 56, 58],
  [66, 72, 72, 76, 76, 76, 82, 85, 90, 96],
]
search_element = 56
assert s.searchMatrix(A, search_element) == 1


'''
search_element = 21
assert s.searchMatrix(A, search_element) == 0
search_element = 7
assert s.searchMatrix(A, search_element) == 1
search_element = 3
assert s.searchMatrix(A, search_element) == 1
search_element = 30
assert s.searchMatrix(A, search_element) == 1
'''


