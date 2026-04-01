class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # main aim is to go over the numbers and idenfity how many 
        # sequences can be made

        # we can think in terms of start of the sequences
        # think what makes a number the start of a sequence
        # -> if there is no number left to that number in the given array
        # for example: 2,3,4. 2 is the start because there is no 1 in the array

        # so we try to build sequence and count the length of the longest one
        # steps:
        # 1. use a set for O(1) lookup
        # 2. for num in nums:
            # check if num is the first number in sequence: (num - 1) not in set
            # if first, build the sequence
                # keep checking if num + 1 is in the array and keep building the
                # array unless it hits a number not in the array
                # count the length of the sequences
                # update max length with curr length
            # if not first, just continue

        # implementation

        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                # sequence started!
                # current length of the sequence
                length = 1
                # check if next number is in set
                while (num + length) in numSet:
                    length += 1
                # update the longest seq length
                longest = max(length, longest)
        
        return longest


