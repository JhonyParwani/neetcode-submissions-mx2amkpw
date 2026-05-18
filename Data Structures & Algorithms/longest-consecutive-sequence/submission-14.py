class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start=0
        end=1
        count=1
        diff=1
        nums_set=set(nums)
        final=[]
        for num in nums_set:
            final.append(num)
        print(final)
        final.sort()
        if len(final)==0:
            return 0
        while end<len(final):
            if final[start]+diff==final[end]:
                end+=1
                diff+=1
            else:
                start=end
                end=start+1
                diff=1
            count=max(count,end-start)
        return count


        