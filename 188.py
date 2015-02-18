class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        peak=[]
        profit=0
        i=0
        while i<len(prices)-1:
            if prices[i]==prices[i+1]:
                del prices[i]
            else:
                i+=1
        for i in range(1,len(prices)-1):
            if prices[i]>prices[i+1] and prices[i]>prices[i-1]:
                peak.append(prices[i])
            elif prices[i]<prices[i+1] and prices[i]<prices[i-1]:
                peak.append(prices[i])
        if prices[-1]>=prices[-2]:
            peak.append(prices[-1])
        
                
        print(peak)
        return 1
s=Solution()
s.maxProfit(1,[10,5,7,10,7,6,7,10,10,10,9,12,12,13])

                
