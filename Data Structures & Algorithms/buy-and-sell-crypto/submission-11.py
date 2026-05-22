class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start=0
        end=0
        maxi=0
        while start<len(prices)-1 and end<len(prices)-1:
            if prices[start]<prices[end]:
                end+=1
            else:
                start=end
                end=start+1
            profit=prices[end]-prices[start]
            maxi=max(maxi,profit)
            print(prices[start],prices[end])
        return maxi




        
        