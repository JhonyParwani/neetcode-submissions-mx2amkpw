class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums=list(set(nums))
        i=0
        final=[]
        nums.sort()
        print(nums)

        while i <len(nums)-2:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]>-(nums[i]):
                    k-=1
                elif nums[j]+nums[k]<-(nums[i]):
                    j+=1
                else:
                    final.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
            i+=1
        return final
            


        