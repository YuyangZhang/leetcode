class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        for letter in sorted(set(s)):
            rest = s[s.index(letter):]
            if set(rest) == set(s):
                return letter + self.removeDuplicateLetters(rest.replace(letter,''))
        return ''