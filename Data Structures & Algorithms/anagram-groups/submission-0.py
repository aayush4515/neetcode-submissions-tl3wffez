class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # idea: keep track of apperances of letters in each string
        # use ord and the fact that alphabet has 26 letters
        # ordinality can be used
        # create a dictionary and use it to map:
            # keys: count of ordinality of the sre, values: list of anagrams
        # result = {}; append the anagram list here

        result = defaultdict(list)
        
        for str in strs:
            count = [0] * 26    # create 26 fields and set all of them to 0 initially
            for ch in str:
                count[ord(ch) - ord('a')] += 1
            result[tuple(count)].append(str)
    
        return list(result.values())
