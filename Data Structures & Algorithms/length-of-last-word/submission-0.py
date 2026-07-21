class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        final=s.split()
        print(final)
        return len(final[-1])
        