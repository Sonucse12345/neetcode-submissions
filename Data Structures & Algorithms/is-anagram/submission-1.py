class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1= {}
        dict2= {}
        for char1 in s:
            if char1 in dict1:
                dict1[char1] +=1
            else:
                dict1[char1] =1
        
        for char2 in t:
            if char2 in dict2:
                dict2[char2] +=1
            else:
                dict2[char2] =1

        if dict1 == dict2:
            return True
        else:
            return False
        

