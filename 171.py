class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        r=''
        num=0
        for i in range(0,len(s)):
            r+=s[-i-1]
        for i in range(0,len(s)):
            num+=(ord(r[i])-ord('A')+1)*pow(26,i)
        return num
s=Solution()
print(s.titleToNumber('A'))
