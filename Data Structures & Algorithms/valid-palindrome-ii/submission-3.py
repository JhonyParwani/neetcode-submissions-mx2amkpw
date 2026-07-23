class Solution:
    def validPalindrome(self, s: str) -> bool:
        check=s
        for i in s:
            check=check.replace(i,"")
            print(check,check[::-1])
            if check==check[ : : -1]:
                return True
            check=s
        return False
        