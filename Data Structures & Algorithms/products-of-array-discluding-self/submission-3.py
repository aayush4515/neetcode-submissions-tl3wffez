class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # forward_product = []
        # backward_product = []

        # # create forward array
        # prev = 1
        # curr_product = 1
        # for num in nums:
        #     forward_product.append(prev * curr_product)
        #     curr_product = prev * curr_product
        #     prev = num
        # print(forward_product)

        # # create backward array
        # prev = 1
        # curr_product = 1
        # for num in reversed(nums):
        #     backward_product.append(prev * curr_product)
        #     curr_product = prev * curr_product
        #     prev = num
        
        # backward_product.reverse()
        
        # # combine both arrays
        # res = []
        # for val1, val2 in zip(forward_product, backward_product):
        #     res.append(val1 * val2)
        # return res

        forward = []
        backward = []

        # create the forward array
        prev = 1
        curr_product = 1
        for num in nums:
            forward.append(prev * curr_product)
            curr_product = prev * curr_product
            prev = num
        
        # create the backward array
        prev = 1
        curr_product = 1
        for num in reversed(nums):
            backward.append(prev * curr_product)
            curr_product = prev * curr_product
            prev = num
        backward.reverse()
        
        # combine both arrays and return the result
        res = []
        for val1, val2 in zip(forward, backward):
            res.append(val1 * val2)
        
        return res





















