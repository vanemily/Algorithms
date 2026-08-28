class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = [0] * len(nums)
        size = len(nums)
        right = size - 1
        left = 0

        for i in range(size):
            if abs(nums[left]) > abs(nums[right]):
                result[size - (i + 1)] = nums[left] * nums[left]
                left += 1
            else:
                result[size - (i + 1)] = nums[right] * nums[right]
                right -= 1
        
        return result
    
# La complejidad espacial es: 0(n) porque estamos creando una lista de tamaño n para almacenar los resultados.
# La complejidad temporal es: 0(n) porque estamos recorriendo la lista de entrada. 

print(Solution().sortedSquares([-4, -1, 0, 3, 10]))  # Output: [0, 1, 9, 16, 100]
