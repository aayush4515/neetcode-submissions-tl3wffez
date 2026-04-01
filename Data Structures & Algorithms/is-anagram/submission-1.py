class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f_map1 = dict()
        f_map2 = dict()

        for ch in s:
            f_map1[ch] = f_map1.get(ch, 0) + 1
        for ch in t:
            f_map2[ch] = f_map2.get(ch, 0) + 1
        
        return f_map1 == f_map2