class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < len(nums) - 1:
                if nums[i] + nums[left] + nums[right] == 0:
                    temp = [nums[i], nums[left], nums[right]]
                    temp.sort()
                    temp = tuple(temp)
                    res.add(temp)
                right -= 1

                if left == right:
                    right = len(nums) - 1
                    left += 1
        
        output = []
        for item in res:
            output.append(list(item))

        return output

        