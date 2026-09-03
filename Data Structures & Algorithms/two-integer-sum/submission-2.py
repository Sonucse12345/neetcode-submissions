class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}#number and index
        for i, val in enumerate(nums):
            complement = target- val
            if complement in diff:
                return [diff[complement],i]
            diff[val] = i


