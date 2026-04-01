class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        
        for key, val in freq.items():
            bucket[val].append(key)
        
        # find the top k elements
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result