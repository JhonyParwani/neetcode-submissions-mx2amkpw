class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final=""
        length=0
        for i in strs[0]:
            for j in range(1,len(strs)):
                if length<len(strs[j])and i==strs[j][length]:
                    pass
                else:
                    return final
            print(i)
            final+=i
            length+=1
        return final

            

        