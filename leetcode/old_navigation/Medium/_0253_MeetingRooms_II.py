"""
253. Meeting Rooms II

Question

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

For example, Given [[0, 30],[5, 10],[15, 20]], return 2.
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.start)
        heap = []
        for i in intervals:
            if heap and i.start >= heap[0]:
                # two meetings can use the same room
                heapq.heapreplace(heap, i.end)
            else:
                # a new room is allocated
                heapq.heappush(heap, i.end)

        return len(heap)
