class Solution:
    def isPalindrome(self, s: str) -> bool:
        final=""
        for char in s:
            if char.isalnum():
                final=final+char.lower() 
        print(final)  
      
        if final==final[: : -1]:
            return True
        else:
            return False