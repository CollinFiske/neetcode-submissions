class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for val in nums:
            if val in vals:
                vals[val] += 1
            else:
                vals[val] = 1
        
        for v in vals:
            if vals[v] > 1:
                return True
        return False