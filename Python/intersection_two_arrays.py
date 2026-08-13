class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if len(nums1) <= len(nums2):
            min_list = nums1
            max_list = nums2
        else:
            min_list = nums2
            max_list = nums1

        unique_nums1 = set(min_list)
        unique_nums = set()

        for i in max_list:
            if i in unique_nums1:
                unique_nums.add(i)

        return list(unique_nums)


print(Solution().intersection([1, 2, 2, 1], [2, 2])) 

### First set:   O(k)
### Second set:  O(k)
###             O(k) + O(k) -> O(2k) --> O(k). -> k = min(n, m) where n and m are the lengths of the two input lists.


    