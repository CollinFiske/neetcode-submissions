class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map: # closer
                top = stack.pop() if stack else '#'

                if bracket_map[char] != top:
                    return False
            
            else: # opener
                stack.append(char)
            

        return not stack