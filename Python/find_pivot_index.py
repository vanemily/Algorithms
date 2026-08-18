class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        left_sum = 0
        right_sum = 0
        
        for i in range(size):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i + 1:])
            
            if left_sum == right_sum:
                return i

        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
