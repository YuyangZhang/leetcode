class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        indices=[]
        length=len(L[0])*len(L)
        Slength=len(S)
        start=0
        for i in range(0,Slength):
            SS=S[start:]
            flag=0
            firt=0
            for word in L:
                if SS.find(word)!=-1:
                    if flag==0:
                        first=SS.find(word)
                    flag=1
            if flag==1:
                if judge(SS[first:first+length],L):
                    indices.append(first+start)
            start+=1
        return list(set(indices))
def judge(s,L):
    l=[0]*len(L)
    for i in range(0,len(L)):
        l[i]=L[i]
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
print(Solution().findSubstring('dddsdfsbfssdfsbfss',['sdfs','bfss']))
