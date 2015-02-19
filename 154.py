class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def findMin(self, num):
        return findPeak(num,0,len(num)-1)


def findPeak(A,start,end):
    if A[start]<A[end] or start==end:
        return A[start]
    else:
        if end-start==1:
            return A[end]
        elif A[int((start+end)/2)]>A[int((start+end)/2)+1]:
            return A[int((start+end)/2)+1]
        else:
            return min(findPeak(A,start,int((start+end)/2)),findPeak(A,int((start+end)/2)+1,end))
    

s=Solution()
print(s.findMin([3,4,4,4,4,4,4,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,10,10,10,-10,-10,-10,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-4,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-1,-1,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3]))
