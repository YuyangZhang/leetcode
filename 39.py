class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        level=0
        index=0
        results=[]
        remain=target
        lastIndex={}
        result=[]
        candidates=sorted(candidates)
        while True:
            #print(remain)
            #print(level)
            #print(candidates[index])
            #print(result)
            #print(lastIndex)
            while index>len(candidates)-1:
                level-=1
                if level<0:
                    break
                remain+=result.pop()
                index=lastIndex[level]+1
                
            if level<0:
                break
            if candidates[index]==remain:
                result.append(candidates[index])
                tmp=[]
                for i in result:
                    tmp.append(i)
                if tmp not in results:
                    results.append(tmp)
                level-=1
                if level<0:
                    break
                index=lastIndex[level]+1
                result.pop()
                remain+=result.pop()
                index=lastIndex[level]+1
            elif candidates[index]>remain:
                level-=1
                if result==[]:
                    break
                remain+=result.pop()
                index=lastIndex[level]+1
            else:
                remain=remain-candidates[index]
                level+=1
                result.append(candidates[index])
                lastIndex[level-1]=index
        return results
            
print(Solution().combinationSum([2,3,7],18))
