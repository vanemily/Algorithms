class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicates = set()

        for number in nums:
            if number in duplicates: 
                return True
            duplicates.add(number)
        return False


## Time complexity: O(n), where n is the length of the input list nums. We iterate through the list once, and each lookup and insertion operation in a set takes O(1) time on average.
## Space complexity: O(n), where n is the length of the input list nums. In the worst case, if all elements are unique, we will store all n elements in the set.

print(Solution().containsDuplicate([1, 2, 3, 4, 5]))  # Output: False
print(Solution().containsDuplicate([1, 2, 3, 4, 1]))  # Output: True
print(Solution().containsDuplicate([]))  # Output: False
print(Solution().containsDuplicate([1, 1, 1, 1, 1]))  # Output: True
print(Solution().containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))  # Output: True