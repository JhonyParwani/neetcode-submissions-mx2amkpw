class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        startzero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[i]
                nums[i]=nums[startzero]
                nums[startzero]=temp
                print(nums[i])
                startzero+=1
        
        