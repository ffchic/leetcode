# 拓展法
"""
扩展法，每次新加一个数然后将原本的每个list重新append这个数
[]
[1] # 新加1，然后在这个空list中append1
[2],[1,2] # 新加2，然后在空list中append2,在[1]中append2
[3],[1,3],[2,3],[1,2,3] # 新加3，在之前的list [],[1],[2],[1,2]分别都加入一个3

"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            temp = []
            for r in result:
                res = r[:]  # copy,防止引用传递
                res.append(num)
                temp.append(res)
            for i in temp:
                result.append(i)
        return result


# 回溯法
"""
回溯法，按照可能出现的长度分别添加对应的list

"""
class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        result.append([])
        for i in range(1,len(nums)+1):
            self.backbracking(nums,result,i,0,[])
        return result


    def backbracking(self,nums,result,length,index,sub):
        if len(sub) == length:
            result.append(sub[:])
            return
        for i in range(index,len(nums)):
            sub.append(nums[i])
            self.backbracking(nums,result,length,i+1,sub)
            sub.pop()

s = Solution2().subsets([1,2,3])
print(s)