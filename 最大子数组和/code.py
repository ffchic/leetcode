"""
分治法，按照左中右分别取最大值
"""
class Solution:
    def maxSubArray(self, nums):
        l = 0
        r = len(nums) - 1
        return self.getMax(nums, l, r)

    def getMax(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = l + ((r - l) // 2)
        left_max = self.getMax(nums, l, mid)
        right_max = self.getMax(nums, mid + 1, r)
        cross_max = self.getCrossMax(nums, l, r, mid)
        return max(left_max, right_max, cross_max)

    def getCrossMax(self, nums, l, r, mid):
        left_sum = nums[mid]
        left_max = left_sum
        for i in range(mid - 1, l-1, -1):
            left_sum += nums[i]
            left_max = max(left_sum, left_max)
        right_sum = nums[mid + 1]
        right_max = right_sum
        for i in range(mid + 2, r+1):
            right_sum += nums[i]
            right_max = max(right_sum, right_max)
        return max(right_max + left_max, left_max, right_max)


s = Solution()
print(s.maxSubArray([5,4,-1,7,8]))