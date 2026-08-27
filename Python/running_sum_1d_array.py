class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        current_sum = 0
        size = len(nums)
        result = [0] * size

        for i in range(size): 
            current_sum += nums[i]
            result[i] = current_sum

        return result


# La complejidad espacial es: 0(n) porque estamos creando una lista de tamaño n para almacenar los resultados.
# La complejidad temporal es: 0(n) porque estamos recorriendo la lista de entrada una vez para calcular la suma acumulativa.

print(Solution().runningSum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]