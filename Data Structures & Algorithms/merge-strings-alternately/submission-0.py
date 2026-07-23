class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first=0
        second=0
        final=""

        while first<len(word1) and second<len(word2):
            final+=word1[first]
            first+=1
            final+=word2[second]
            second+=1
        if first<len(word1):
            while first<len(word1):
                final+=word1[first]
                first+=1
        if second<len(word2):
            while second<len(word2):
                final+=word2[second]
                second+=1
        return final







        