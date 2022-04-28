#
# Created on Thu Apr 28 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a collection of intervals, merge all overlapping intervals.

Problem Constraints
1 <= Total number of intervals <= 100000.

Input Format
First argument is a list of intervals.

Output Format
Return the sorted list of intervals after merging all the overlapping intervals.

Example Input
Input 1:
    [1,3],[2,6],[8,10],[15,18]

Example Output
Output 1:
    [1,6],[8,10],[15,18]

Example Explanation
Explanation 1:
    Merge intervals [1,3] and [2,6] -> [1,6].
    so, the required answer after merging is [1,6],[8,10],[15,18].
    No more overlapping intervals present.
'''
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        n = len(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        mergedIntervals = []

        for i in range(1, n):
            s = intervals[i][0]
            e = intervals[i][1]

            if s <= end:
                #start will remain same
                end = max(end, e)
            else:
                mergedIntervals.append([start, end])
                start = s
                end = e
        mergedIntervals.append([start, end])
        return mergedIntervals

####################  for Scaler OOP   #####################

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution1:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge1(self, intervals):
        n = len(intervals)
        intervals = sorted(intervals, key = lambda x: x.start)
        
        start = intervals[0].start
        end = intervals[0].end
        
        mergedIntervals = []
        
        for i in range(1, n):
            s = intervals[i].start
            e = intervals[i].end

            if s <= end:
                #start will remain same
                end = max(end, e)
            else:
                mergedIntervals.append(Interval(start, end))
                start = s
                end = e
        mergedIntervals.append(Interval(start, end))
        return mergedIntervals

s = Solution()
A = [[1,3],[2,6],[8,10],[15,18]] #[[1, 6], [8, 10], [15, 18]]
A = [[1,2],[2,4],[5,8],[7,10]] #[[1, 4], [5, 10]]
A = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
ans = s.merge(A)
print(ans)

            


