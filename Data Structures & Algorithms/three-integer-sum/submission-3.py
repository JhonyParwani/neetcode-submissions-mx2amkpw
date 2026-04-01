class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        first=0
        final_list=set()
        final=[]
        nums.sort()
        for i in range(n-2):
            middle=i+1
            last=n-1

            while middle<last:
                if nums[i]+nums[middle]+nums[last]>0:
                    last-=1
                elif nums[i]+nums[middle]+nums[last]<0:
                    middle+=1
                else:
                    final_list.add((nums[i],nums[middle],nums[last]))
                    last-=1
                    middle+=1
        
        return [ list(t)   for t in  final_list]
        