class Solution:
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        l = 0
        r = len(nums) - 1
        while l < r :
            mid = l+(r-l)//2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                return mid
        return l if nums[l] >= target else l + 1

