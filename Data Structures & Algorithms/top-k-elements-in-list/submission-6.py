class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        bucket = [[] for _ in range(len(nums) + 1)]
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # create the bucket, indices = no. of repetitions, values = list of numbers
        for key, value in freq_map.items():
            bucket[value].append(key)
    
        # get the k frequent elements
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
            if len(result) == k:
                return result
        