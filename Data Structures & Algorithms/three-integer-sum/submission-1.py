class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < len(nums) - 1:
                if nums[i] + nums[left] + nums[right] == 0:
                    temp = [nums[i], nums[left], nums[right]]
                    temp.sort()
                    if temp not in res:
                        res.append(temp)
                right -= 1

                if left == right:
                    right = len(nums) - 1
                    left += 1

        return res

        