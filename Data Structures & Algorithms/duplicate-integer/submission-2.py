class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1={}
        for num in nums:
            if num in dict1:
                dict1[num] +=1
            else:
                dict1[num] =1
        for key, value in dict1.items():
            if dict1[key]>= 2:
                return True
        return False
        