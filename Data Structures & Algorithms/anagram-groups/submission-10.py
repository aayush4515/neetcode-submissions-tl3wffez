class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = defaultdict(list) # keys: freq map, values: lists of identical freq maps

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # append the string
            visited[tuple(count)].append(s)
        
        return list(visited.values())
