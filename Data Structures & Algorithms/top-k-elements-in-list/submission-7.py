class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for i in range(len(nums) + 1)]
        
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for key, val in freq_map.items():
            freq[val].append(key)
        
        # print the k most frequent elements
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
            if len(result) == k:
                return result