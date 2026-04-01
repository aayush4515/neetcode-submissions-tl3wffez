class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # y = target - x; x -> each num in nums
        
        # stores the number and its index
        visited = {}

        for i, x in enumerate(nums):
            y = target - x
            if y in visited:
                return [visited[y], i]
            visited[x] = i
        return

