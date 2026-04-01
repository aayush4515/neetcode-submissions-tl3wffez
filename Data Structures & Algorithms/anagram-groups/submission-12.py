class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        visited = defaultdict(list) # key: frequency map, value: list of identical frequency map

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            visited[tuple(count)].append(s)
        
        return list(visited.values())

        