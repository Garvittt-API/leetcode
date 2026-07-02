class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0
        match_idx = 0
        star_idx = -1
        
        s_len, p_len = len(s), len(p)
        
        while s_ptr < s_len:
            # Case 1: Characters match, or pattern has '?'
            if p_ptr < p_len and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            
            # Case 2: Pattern has a '*', record the checkpoint
            elif p_ptr < p_len and p[p_ptr] == '*':
                star_idx = p_ptr
                match_idx = s_ptr
                p_ptr += 1  # Try matching 0 characters first
                
            # Case 3: Mismatch, but we have a previous '*' to backtrack to
            elif star_idx != -1:
                p_ptr = star_idx + 1  # Reset pattern to right after the star
                match_idx += 1        # Advance string pointer to let the star absorb it
                s_ptr = match_idx     # Restart matching from here
                
            # Case 4: Mismatch and no '*' to save us
            else:
                return False
                
        # Check for remaining trailing stars in the pattern
        while p_ptr < p_len and p[p_ptr] == '*':
            p_ptr += 1
            
        # If we reached the end of the pattern, it's a match
        return p_ptr == p_len