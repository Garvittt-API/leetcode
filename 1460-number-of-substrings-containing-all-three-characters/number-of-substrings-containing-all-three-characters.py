class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Store the last seen index of 'a', 'b', and 'c'
        # Initialize with -1 to indicate they haven't been seen yet
        last_seen = [-1, -1, -1]
        result = 0
        
        for i, char in enumerate(s):
            # Update the last seen index for the current character
            # ord(char) - ord('a') maps 'a'->0, 'b'->1, 'c'->2
            last_seen[ord(char) - ord('a')] = i
            
            # The number of valid substrings ending at 'i' is the minimum 
            # of the last seen indices of 'a', 'b', and 'c'.
            # If all have been seen at least once, the valid substrings
            # start from any index up to min(last_seen).
            result += min(last_seen) + 1
            
        return result