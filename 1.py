class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dic={}
        for i in range(0,len(num)):
            dic[i+1]=num[i]
        Snum=sorted(dic.items(), key=lambda d:d[1])
        print(Snum)
        for i in range(0,len(num)):
            for j in range(i+1,len(num)):
                if Snum[i][1]+Snum[j][1]==target:
                    if Snum[i][0]>Snum[j][0]:
                        return (Snum[j][0],Snum[i][0])
                    else:
                        return (Snum[i][0],Snum[j][0])
                elif Snum[i][1]+Snum[j][1]>target:
                    break
s=Solution()           
print(s.twoSum([0,4,3,0],0))
