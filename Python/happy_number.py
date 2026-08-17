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
# Incluso cuando son los digitos, el numero máximo del digito es 9, incluso teniendo 100 digitos, si el número máximo de d es 9, y el doble de 9 es 81
# tendriamos 100 * 81 = 8,100, que es un número de 5 digitos que incluso disminuye considerablemente el tamaño, por lo que es más rápido que encontremos 1 o entremos en un ciclo.

print(Solution().isHappy(19))  # Output: True
    