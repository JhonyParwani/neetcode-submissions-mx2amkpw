class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sort=sorted(nums)
        first=0
        last=len(nums)-1
        



        while last != first:
            if nums_sort[first] + nums_sort[last]> target:
                last-=1
            elif nums_sort[first] + nums_sort[last]< target:
                first+=1
            else:
                first_value=nums_sort[first]
                second_value=nums_sort[last]
                break
        print(first_value,second_value)
        final=[]
        for i,num in enumerate(nums):
            if num==first_value or num==second_value:
                final.append(i)
        return final
            

        