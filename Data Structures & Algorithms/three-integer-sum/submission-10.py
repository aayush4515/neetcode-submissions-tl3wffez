class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # seen = set()
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         continue
        #     seen.add(nums[i])
        #     left = i + 1
        #     right = len(nums) - 1
        #     while left < right:
        #         if nums[i] + nums[left] + nums[right] == 0:
        #             temp = (nums[i], nums[left], nums[right])
        #             res.add(temp)
        #         right -= 1

        #         if left == right:
        #             right = len(nums) - 1
        #             left += 1
        
        # output = []
        # for item in res:
        #     output.append(list(item))

        # return output



        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    #right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
        