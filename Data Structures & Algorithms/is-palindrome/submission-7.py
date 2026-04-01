class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1

        while first < last:
            if s[first].isalnum() == False:
                first += 1
                continue
            if s[last].isalnum() == False:
                last -= 1
                continue
            
            if s[first].lower() == s[last].lower():
                first += 1
                last -= 1
            else:
                return False
        
        return True
        