class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda k:k[0])
        result = []
        for i in intervals:
            if not result or result[-1][1] < i[0]:
                result.append(i)
            else:
                result[-1][1] = i[1]
        return result

s = Solution()
print(s.merge([[1,4],[0,4]]))