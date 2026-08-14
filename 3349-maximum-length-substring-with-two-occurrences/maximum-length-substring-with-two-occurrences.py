class Solution(object):
    def maximumLengthSubstring(self, s):
        freq = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char, 0) + 1
            
            while freq[char] > 2:
                left_char = s[left]
                freq[left_char] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len
