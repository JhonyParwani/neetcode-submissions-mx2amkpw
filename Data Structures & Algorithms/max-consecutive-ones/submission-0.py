class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==0:
                count=0
            else:
                count+=1
            maxi=max(maxi,count)
            
        return maxi
            
        