class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize our result array with 1s
        res = [1] * n
        
        # Pass 1: Calculate the prefix products (left of current element)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Calculate the postfix products (right of current element) 
        # and multiply them with the stored prefixes
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res