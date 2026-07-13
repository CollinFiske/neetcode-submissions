class Solution:
    def climbStairs(self, n: int) -> int:
        # Quick exit for the base cases you correctly identified
        if n <= 3:
            return n
            
        # Create an array of size n + 1, filled with zeros
        steps = [0] * (n + 1)
        
        # Manually set the base cases
        steps[1] = 1
        steps[2] = 2
        
        # Start calculating from step 3 up to n
        for i in range(3, n + 1):
            steps[i] = steps[i-1] + steps[i-2]
            
        return steps[n]