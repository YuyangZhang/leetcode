class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        newNum=[]
        gap=0
        if len(num)<2:
            return 0
        for i in range(0,len(num)):
            n=num[i]
            if len(newNum)==0:
                newNum.append(n)
            else:
                newNum=insertSort(newNum,n,0,len(newNum)-1)
        for i in range(0,len(newNum)-1):
            if newNum[i+1]-newNum[i]>gap:
                gap=newNum[i+1]-newNum[i]
                
        return gap
def insertSort(num,n,start,end):
    tmp=num
    mid=int((end+start)/2)
    if start==end:
        if n>=tmp[start]:
            tmp.insert(start+1,n)
            return tmp
        else:
            tmp.insert(start,n)
            return tmp
    if end-start==1:
        if n>=tmp[end]:
            tmp.insert(end+1,n)
            return tmp
        elif n<=tmp[start]:
            tmp.insert(start,n)
            return tmp
        else:
            tmp.insert(end,n)
            return tmp
    if n<=num[mid]:
        return insertSort(num,n,start,mid)
    else:
        return insertSort(num,n,mid+1,end)

print(Solution().maximumGap([1,1,1,1,1,5,8]))
