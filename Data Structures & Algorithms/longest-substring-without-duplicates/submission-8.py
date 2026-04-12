class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        end=1
        count=1
        final=set()
        if len(s)==0:
            return 0
        final.add(s[start])

        while end<len(s):
            if s[end] not in final:
                final.add(s[end])
                end+=1
            else:
                final.remove(s[start])
                start+=1
            count=max(count,len(final))
        return count
            