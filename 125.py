class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        r=''
        rr=''
        s=s.upper()
        for i in range(0,len(s)):
            if s[i].isalnum() or s[i].isalpha():
                r+=s[i]
        for i in range(0,len(r)):
            rr+=r[-1-i]
        if rr==r:
            return True
        else:
            return False
s=Solution()
print(s.isPalindrome('A man, a plan, a canl: Panama'))
