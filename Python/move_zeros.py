class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        size = len(nums)
        left = 0

        for right in range(size):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums

print(Solution().moveZeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]