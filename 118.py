class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        results=[]
        preList=[]
        result=[]
        for i in range(0,numRows+1):
            result=[]
            for j in range(0,i):
                if j==0 or j==i-1:
                    result.insert(j,1)
                else:
                    result.insert(j,preList[j-1]+preList[j])
            if result!=[]:
                results.append(result)
            preList=result[:]
            print(result)
        return results
print(Solution().generate(5))
