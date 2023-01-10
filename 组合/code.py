class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(result, n, k)
        return result

    def backtracking(self, result, n, k,begin=1, list=[]):
        if len(list) == k:
            result.append(list[:])
            return

        for i in range(begin, n+1):

            list.append(i)
            self.backtracking(result,n,k,begin=i+1,list=list)
            list.pop()


s = Solution()
print(s.combine(4,2))