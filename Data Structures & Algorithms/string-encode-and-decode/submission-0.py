class Solution:

    def encode(self, strs: List[str]) -> str:
        outputStr = ""
        
        for string in strs:
            outputStr = outputStr + string + '\n'

        return outputStr
            

    def decode(self, s: str) -> List[str]:
        outputList = []

        startOfStrIndex = 0

        for i, char in enumerate(s):
            if char == '\n':
                endOfStrIndex = i
                outputList.append(s[startOfStrIndex:endOfStrIndex])

                startOfStrIndex = i + 1

        return outputList

