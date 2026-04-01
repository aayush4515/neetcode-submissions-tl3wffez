class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f_map1 = dict()
        f_map2 = dict()

        for char in s:
            f_map1[char] = f_map1.get(char, 0) + 1
        for char in t:
            f_map2[char] = f_map2.get(char, 0) + 1
        
        return f_map1 == f_map2