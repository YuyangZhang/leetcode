class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        p=findPeak(A,0,len(A)-1)
        B=A[p:]+A[:p]
        if A[0]==target:
            return 0
        else:
            return divCon(target,0,len(B)-1,B,A,p)


def findPeak(A,start,end):
    if A[start]<=A[end]:
        return 0
    else:
        if end-start==1:
            return end
        elif A[int((start+end)/2)]>A[int((start+end)/2)+1]:
            return int((start+end)/2)+1
        else:
            return max(findPeak(A,start,int((start+end)/2)),findPeak(A,int((start+end)/2)+1,end))
    

def divCon(target,lowIndex,highIndex,A,B,p):
    if p==0:
        if target==A[lowIndex]:
            if target<B[0]:
                return lowIndex
            else:
                return lowIndex
        elif target==A[highIndex]:
            if target<B[0]:
                return highIndex
            else:
                return highIndex
        elif target<A[lowIndex]:
            return -1
        elif target>A[highIndex]:
            return -1
        else:
            return max(divCon(target,lowIndex,int((highIndex+lowIndex)/2),A,B,p),divCon(target,int((highIndex+lowIndex)/2)+1,highIndex,A,B,p))
    else:
        if target==A[lowIndex]:
            if target<B[0]:
                return p+lowIndex
            else:
                return lowIndex-len(A)+p
        elif target==A[highIndex]:
            if target<B[0]:
                return p+highIndex
            else:
                return highIndex-len(A)+p
        elif target<A[lowIndex]:
            return -1
        elif target>A[highIndex]:
            return -1
        else:
            return max(divCon(target,lowIndex,int((highIndex+lowIndex)/2),A,B,p),divCon(target,int((highIndex+lowIndex)/2)+1,highIndex,A,B,p))
    

s=Solution()
print(s.search([12,13,15,1,2,10,11],2))
