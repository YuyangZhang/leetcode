class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num=sorted(num)
        al=1000000
        i=0
        while i<len(num)-2:
            left=i+1
            right=len(num)-1
            cur=100000
            while left!=right:
                summ=num[i]+num[left]+num[right]
                if summ==target:
                    return target
                elif summ<target:
                    left+=1
                    if abs(summ-target)<abs(cur-target):
                        cur=summ
                else:
                    right-=1
                    if abs(summ-target)<abs(cur-target):
                        cur=summ
            if abs(al-target)>abs(cur-target):
                al=cur
            i+=1
        return al
s=Solution()
print(s.threeSumClosest([1,2,4,8,16,32,64,128], 82))
