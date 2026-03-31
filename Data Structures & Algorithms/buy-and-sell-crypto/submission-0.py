class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        w=set()
        l=len(prices)
        
        prof=[]
        
        for i in range(l):
            for j in range(i+1,l):

                if prices[i]<prices[j]:
                    profit=prices[j]-prices[i]
                    prof.append(profit)

        if not prof:
            return 0
        else:
            return max(prof)

           
        
        
        