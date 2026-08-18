class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        left_sum = 0
        right_sum = sum(nums)  
        
        for i in range(size):
            right_sum -= nums[i]
            
            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1

## In the first iteration the time complexity is 0(n^2) because for every element I calculate the sum of the right side and the left side.
## so if the length of the array is n, it will take 0(n)

## The second iteration the time complexity is 0(n) because I calculate the sum of the right side and left side in one iteration.
## The space complexity is 0(1) because I am not using any extra space.

print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
