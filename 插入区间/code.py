class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        placed = False
        for interval in intervals:
            if interval[0] > newInterval[1]:
                if not placed:
                    result.append(newInterval)
                    placed = True
                result.append(interval)
            elif interval[1] < newInterval[0]:
                result.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        if not placed:
            result.append(newInterval)
        return result