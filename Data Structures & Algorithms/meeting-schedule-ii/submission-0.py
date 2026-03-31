"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i: i.start)
        print(intervals)
        minheap = []
        for intervalo in intervals:
            print(intervalo.start, intervalo.end)
            #heapq.heappush(min_heap, interval.end)
            if minheap and minheap[0] <= intervalo.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, intervalo.end)
        return len(minheap)