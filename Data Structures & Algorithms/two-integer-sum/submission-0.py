class Solution:
    def twoSum(self, nums, target): 
        hashmap= {}# in this we storing value  and their indices
        for index, value in enumerate(nums):# inside this handle both if hasmap has value index pain and when dosent have value pair 
            differ= target - value
            if differ not in hashmap:
                hashmap[value] = index
            else:
                 return [hashmap[differ],index]
            
        
nums = [3,4,5,6]
target = 7
sol=Solution()
result= sol.twoSum(nums, target)
print(result)
