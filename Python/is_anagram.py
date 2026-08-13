class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        frecuencies_s = {}
        frecuencies_t = {}

        
        for num in s: 
            if num in frecuencies_s:
                frecuencies_s[num] = frecuencies_s[num] + 1
            else:
                frecuencies_s[num] = 1

        for num in t: 
            if num in frecuencies_t:
                frecuencies_t[num] = frecuencies_t[num] + 1
            else:
                frecuencies_t[num] = 1

        return frecuencies_s == frecuencies_t




print(Solution().isAnagram("anagram", "nagaram"))  # Output: True
print(Solution().isAnagram("rat", "car"))  # Output: False
