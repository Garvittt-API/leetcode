class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Dictionary to keep track of the counts of 'a', 'b', and 'c'
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        result = 0
        n = len(s)
        
        for right in range(n):
            count[s[right]] += 1
            
            # While the current window contains at least one of each character
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                # All substrings starting from 'left' and ending at or after 'right' 
                # are valid. There are (n - right) such substrings.
                result += (n - right)
                
                # Shrink the window from the left
                count[s[left]] -= 1
                left += 1
                
        return result