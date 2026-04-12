class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start=0
        end=1
        n=len(prices)
        profit=0
        while end<n:
            print(prices[end])
            if prices[start]>=prices[end]:
                start=end
                end=start+1
            else:
                profit=max(profit,prices[end]-prices[start])
                end+=1
        return profit


            
        