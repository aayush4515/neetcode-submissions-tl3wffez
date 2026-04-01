class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        prefix = []
        postfix = []

        product = 1
        # compute prefix array
        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(product)
                product *= nums[i]
                continue
            
            prefix.append(product)
            product *= nums[i]
            
        # reset the variable
        product = 1

        # compute postfix array
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix.append(product)
                continue
            product *= nums[i + 1]
            postfix.append(product)
             
        product = 1
        # find product of both arrays and return result
        for i in range(0, len(nums)):
            product = prefix[i] * postfix[len(nums) - i - 1]
            output.append(product)
        
        print(prefix)
        print(postfix)
        return output
        
        
        