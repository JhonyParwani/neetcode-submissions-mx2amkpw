class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        final=[]
        words.sort(key=len)
        print(words)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    final.append(words[i])
        return list(set(final))
        