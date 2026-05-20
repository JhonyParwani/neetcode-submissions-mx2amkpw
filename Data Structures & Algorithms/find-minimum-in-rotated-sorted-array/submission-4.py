class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        minvalue = float("inf")
        last=len(nums)-1
        while start<=last:
            middle=(start+last)//2
            print(start,middle,last)
            minvalue=min(nums[middle],minvalue)
            if nums[middle]>nums[last]:
                start=middle+1
            else:
                last=middle-1
        # print(nums[middle])
        return minvalue


        