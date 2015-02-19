class Solution:
    # @return an integer
    def threeSum(self, num):
        num=sorted(num)
        i=0
        lists=[]
        while i<len(num)-2:
            left=i+1
            right=len(num)-1
            while left!=right:
                summ=num[i]+num[left]+num[right]
                if summ==0:
                    if ([num[i],num[left],num[right]] in lists)==False:
                        lists.append([num[i],num[left],num[right]])
                    left+=1
                elif summ<0:
                    left+=1
                else:
                    right-=1
            i+=1
        return lists
s=Solution()
print(s.threeSum([-2,0,1,1,2]))
