class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        first=0
        last=1
        diff=1
        maxi=1
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        final=[]
        nums_set=set(nums)
        for num in nums_set:
            final.append(num)
        final.sort()
        print(final)
        while last<len(final):
            if final[first]+diff==final[last]:
                last+=1
                diff+=1
            else:
                print(first,last)
                maxi=max(maxi,(last-first))
                first=last
                last=first+1
                diff=1
        maxi=max(maxi,(last-first))
        return maxi
            
