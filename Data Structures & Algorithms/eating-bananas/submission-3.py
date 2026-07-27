class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        left=1
        right=max(piles)
        while left<right:
            mid=(left+right)//2
            hours=0
            for i in piles:
                hours+=ceil(i/mid)
            if hours<=h:
                right=mid
            else:
                left=mid+1
        return left
            



            
            
        