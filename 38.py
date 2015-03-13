class Solution:
    # @return a string
    def countAndSay(self, n):
        s='1'
        index=1
        if n==1:
            return s
        while index<n:
            num=0
            letter=s[0]
            result=''
            for i in range(0,len(s)):
                if i==len(s)-1:
                    if s[i]==letter:
                        num+=1
                        result+=str(num)+str(letter)
                    else:
                        result+=str(num)+str(letter)
                        result+=str(1)+str(s[i])
                else:
                    if s[i]==letter:
                        num+=1
                    else:
                        result+=str(num)+str(letter)
                        num=1
                        letter=s[i]
            s=result
            index+=1
        return s                    
                    
print(Solution().countAndSay(5))
