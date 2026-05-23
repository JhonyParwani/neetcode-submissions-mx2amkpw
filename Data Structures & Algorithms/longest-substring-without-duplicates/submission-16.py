class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        end=0
        count=1
        final=set()
        if len(s)==0:
            return 0

        while end<len(s):
            while s[end] in final:
                final.remove(s[start])
                start+=1
            final.add(s[end])
            print(final)
            end+=1
            count=max(count,len(final))
        return count
            