class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        tChars ={}

        for char in s:
            if char in sChars:
                sChars[char] += 1
            else:
                sChars[char] = 1

        for char in t:
            if char in tChars:
                tChars[char] += 1
            else:
                tChars[char] = 1

        return sChars == tChars