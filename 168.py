class Solution:
    # @return a string
    def convertToTitle(self, num):
        s=''
        i=1
        while num>0:
            s+=chr((num-1)%26+ord('A'))
            num=int((num-1)/26)
            i+=1
        r=''
        for i in range(0,len(s)):
            r+=s[-i-1]
        return r
s=Solution()
print(s.convertToTitle(26*26*26*26))
