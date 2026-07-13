class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
            
        # Convert to a set for O(1) lookups and to remove duplicates
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # ONLY start counting if this is the start of a sequence
            # (e.g., if 3 is in the set, we don't start counting from 4)
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Keep looking for the next consecutive number in the set
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # Update our max streak
                if current_streak > longest:
                    longest = current_streak

        return longest
        