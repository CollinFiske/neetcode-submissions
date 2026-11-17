class Solution:
    def isPalindrome(self, s: str) -> bool:
        #2 pointers converging, compare each and return false is !=, also ignore non alphanumerical chars + deal w/ case insensitive

        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            # Skip non-alphanumeric characters from the right
            if not s[right].isalnum():
                right -= 1
                continue
                
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -=1

        return True

