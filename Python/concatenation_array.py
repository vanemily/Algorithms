class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        result = [0] * (2 * size)

        for i in range(size):
            result[i] = nums[i]
            result[i + size] = nums[i]

        return result


print(Solution().getConcatenation([1, 2, 3]))  # Output: [1, 2, 3, 1, 2, 3]