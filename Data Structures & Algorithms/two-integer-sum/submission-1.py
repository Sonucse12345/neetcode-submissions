class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicto = {}
        for i, num in enumerate(nums):
            diff = target - num
            # Check if the complement exists in the dictionary
            if diff in dicto:
                return [dicto[diff], i]  # Return the indices of the two numbers
            dicto[num] = i  # Store the index of the current number in the dictionary
        return []  # In case no solution is found
