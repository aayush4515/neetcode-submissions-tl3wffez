class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # can use two frequency maps, one for each
        # compare if both of them are equal
        # if equal: True
        # else: False

        dict_s = dict()
        dict_t = dict()

        # frequency maps
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        return dict_s == dict_t