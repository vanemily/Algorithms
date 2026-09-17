class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        size = len(numbers)
        right = size - 1
        left = 0

        while left < right: 
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

# La complejidad espacial es: O(1) porque no estamos la memoria auxiliar no crece proporcionalmente con n

# La complejidad temporal es: O(n) porque estamos recorriendo la lista de entrada.


print(Solution().twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]