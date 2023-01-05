def backtracking(result, nums, visited, list):
    if len(list) == len(nums):
        result.append(list.copy())
        return
    for num in nums:
        if not visited[num]:
            list.append(num)
            visited[num] = True
            backtracking(result,nums,visited,list)
            list.pop()
            visited[num] = False


class Solution:
    def permute(self, nums):
        visited = {}
        result = []
        for i in nums:
            visited[i] = False
        backtracking(result, nums, visited, [])
        return result

s = Solution()
print(s.permute([1,2,3]))