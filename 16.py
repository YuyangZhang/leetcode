class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        return target-opt(num,target,3,0)
    
def opt(num,target,left,start):
    if left==0:
        return target
    if left==len(num)-start:
        return target-sum(num[start:])
    if len(num)-start<left:
        return 10000000
    value=num[start]
    start+=1
    dele=opt(num,target,left,start)
    print('start:'+str(start)+'dele:'+str(dele))
    add=opt(num,target-value,left-1,start)
    print('start:'+str(start)+'add:'+str(add))
    if abs(add)>=abs(dele):
        return dele
    else:
        return add
s=Solution()
print(s.threeSumClosest([0,1,1,1], -100))
