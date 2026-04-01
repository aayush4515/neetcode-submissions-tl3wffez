class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = s.lower()
     
        first = 0
        last = len(s) - 1

        while first < last:
            if new[first].isalnum() == False:
                first += 1
                continue
            if new[last].isalnum() == False:
                last -= 1
                continue
            
            if new[first] == new[last]:
                first += 1
                last -= 1
            else:
                return False
        
        return True
        