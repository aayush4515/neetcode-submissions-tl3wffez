class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, x in enumerate(nums):
            y = target - x
            if y in visited:
                return [visited[y], i]
            visited[x] = i
        return
