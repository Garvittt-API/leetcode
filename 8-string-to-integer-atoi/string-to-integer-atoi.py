class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit signed integer boundaries
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        n = len(s)
        i = 0
        
        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        # If we reached the end of the string, return 0
        if i == n:
            return 0
            
        # Step 2: Determine signedness
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
            
        # Step 3: Conversion & Step 4: Rounding (Overflow handling)
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before multiplying
            # If res > INT_MAX // 10, multiplying by 10 will definitely overflow.
            # If res == INT_MAX // 10, adding a digit greater than 7 (or 8 for negative) overflows.
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
                
            res = res * 10 + digit
            i += 1
            
        return sign * res