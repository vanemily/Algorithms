class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sum_squares(n)

        return n == 1

    def sum_squares(self, n):
        total = 0

        for digit in str(n):
            total += int(digit) ** 2
        
        return total

## La complejidad espacial y temporal de este algoritmo es O(log n).
## porque recorre los digitos de n, la cantidad de digitos de un entero crece logaritmicamente con respecto a su valor de n

print(Solution().isHappy(19))  # Output: True
    