class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = set()
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    temp = (nums[i], nums[left], nums[right])
                    res.add(temp)
                right -= 1

                if left == right:
                    right = len(nums) - 1
                    left += 1
        
        output = []
        for item in res:
            output.append(list(item))

        return output

        