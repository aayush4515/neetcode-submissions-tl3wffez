class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # approach 1
        # use a hash set
        # set removes all the duplicates
        # compare the length of the set and the original list
        # if len(set) < len(nums): return true

        # return len(set(nums)) < len(nums)

        # approach 2
        # use a new hash set, call it seen
        # keep checking if the current digit already appears in see
        # if it does: return True
        # else: move forward

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
