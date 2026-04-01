class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a hash set
        # set removes all the duplicates
        # compare the length of the set and the original list
        # if len(set) < len(nums): return true

        return len(set(nums)) < len(nums)