class Solution:

    def encode(self, strs: List[str]) -> str:
        res =""#for storing encoded string
        for s in strs:
            res += str(len(s))+ "#"+s  + "#"#each string in s encode enoded in form of lengeth of that string #original string of strs

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Extract length substring and convert to integer
            i = j + 1  # Move i past the '#'
            j = i + length  # Calculate end index of substring
            res.append(s[i:j])  # Append decoded string to result list
            i = j + 1  # Move i past the end of current substring
        return res




# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         return " ".join(strs)
#     def decode(self, s: str) -> List[str]:
#         return str.split(" ")