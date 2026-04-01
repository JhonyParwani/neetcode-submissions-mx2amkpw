class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(len(s))
        final=[]
        for i in s:
            if i.isalnum():
                final.append(i)
        s="".join(final)
        print(s)
        print(s[::-1])
        if s.lower()==s[::-1].lower():
            return True
        else:
            return False
        