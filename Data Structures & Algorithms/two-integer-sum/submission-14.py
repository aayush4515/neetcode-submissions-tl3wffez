class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, num in enumerate(nums):
            y = target - num
            if y in visited:
                return [visited[y], i]
            visited[num] = i
        return