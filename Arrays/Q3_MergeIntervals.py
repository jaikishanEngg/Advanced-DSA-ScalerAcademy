#
# Created on Fri May 13 2022
# Copyright (c) 2022 Scaler Academy #DSA
# @author JaiKishan
#
'''
Problem Description
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Problem Constraints
0 <= |intervals| <= 105

Input Format
First argument is the vector of intervals
second argument is the new interval to be merged

Output Format
Return the vector of intervals after merging

Example Input
Input 1:
    Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
Input 2:
    Given intervals [1, 3], [6, 9] insert and merge [2, 6] .

Example Output
Output 1:
    [ [1, 5], [6, 9] ]
Output 2:
    [ [1, 9] ]

Example Explanation
Explanation 1:
    (2,5) does not completely merge the given intervals
Explanation 2:
    (2,6) completely merges the given intervals
'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
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

#We have already solved a similar problem in HomeWork - HW_Q3_MergeOverlappingIntervals.py
