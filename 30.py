import copy
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        indices=[]
        length=len(L[0])*len(L)
        Slength=len(S)
        start=0
        lfirst=0
        while start<len(S):
            SS=S[start:]
            flag=0
            first=0
            for word in L:
                if SS.find(word)!=-1:
                    if flag==0:
                        first=SS.find(word)
                    flag=1
            if flag==1:
                if judge(SS[first:first+length],L):
                    indices.append(first+start)
            start=first+1+lfirst
            lfirst=first
            if lfirst==0:
                break
        return list(set(indices))
def judge(s,L):
    l=copy.copy(L)
    if s=='':
        if L==[]:
            return True
        else:
            return False
    else:
        length=len(l[0])
    if s[0:length] not in l:
        return False
    else:
        l.remove(s[0:length])
        return judge(s[length:],l)
print(Solution().findSubstring('mississippi',['mississippis']))
