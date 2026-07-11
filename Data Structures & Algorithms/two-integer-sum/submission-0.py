class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myset = {}
        for i in range(len(nums)):
            myset[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]
            if y in myset and myset[y] != i:
                return [i, myset[y]]

