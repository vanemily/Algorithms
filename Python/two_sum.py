class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for index, num in enumerate(nums):
            current_target = target - num 
            
            if current_target in seen:
                return [seen[current_target], index]

            seen[num] = index


## Time complexity: O(n), where n is the length of the input list nums. We iterate through the list once, and each lookup and insertion operation in a dictionary takes O(1) time on average.
## Space complexity: O(n), where n is the length of the input list nums. In the worst case, if all elements are unique, we will store all n elements in the dictionary.

print(Solution().twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(Solution().twoSum([3, 2, 4], 6))  # Output: [1, 2]
print(Solution().twoSum([3, 3], 6))  # Output: [0, 1]
