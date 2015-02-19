class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        B=list(set(A))
        return find(B,target,0,len(B)-1)


def find(A,target,start,end):
    if A==[]:
        return False
    if start+1<len(A):
        if A[start]==A[start+1]:
            del A[start]
            return find(A,target,start,end-1)
    if end-1>0:
        if A[end]==A[end-1]:
            del A[end]
            return find(A,target,start,end-1)
    if start==end:
        if target==A[end]:
            return True
        else:
            return False
    if A[start]==A[end]:
        del A[end]
        return find(A,target,start,end-1)
    elif A[start]<A[end]:
        if target<A[start] or target>A[end]:
            return False
        else:
            return find(A,target,start,int((start+end)/2)) or find(A,target,int((start+end)/2)+1,end)
    else:
        return find(A,target,start,int((start+end)/2)) or find(A,target,int((start+end)/2)+1,end)
s=Solution()
print(s.search([0,0,1,1,2,0],2))
