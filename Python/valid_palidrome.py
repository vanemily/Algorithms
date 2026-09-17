
import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        new_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        size = len(new_string)
        right = size - 1
        left = 0  
        
        while left < right:
            if new_string[left] != new_string[right]:
                return False
            left += 1
            right -= 1

        return True

# La complejidad Time es: 0(n):
#   - Primero se recorre el string para normalizarlo y después se recorre máximo la mitad con dos apuntadores:
#    O(n) + O(n/2) = O(n)

# La complejidad espacial es: O(n):
#   Porque se crea una lista nueva, que en el peor de los casos puede contener los n caracteres del string original.

print (Solution().isPalindrome("A man, a plan, a canal: Panama"))  # Output: True