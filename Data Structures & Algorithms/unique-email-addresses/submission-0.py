class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        finallist=[]
        for email in emails:
            final=email.split('@')
            first=final[0].split('+')
            first=first[0].replace(".","")
            finallist.append(first+final[1])
        return len(set(finallist))
            
            