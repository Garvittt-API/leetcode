class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Convert to string to inspect each digit
        s = str(n)
        
        filtered_digits = []
        digit_sum = 0
        
        for char in s:
            if char != '0':
                filtered_digits.append(char)
                digit_sum += int(char)
        
        # Edge case: if no non-zero digits are found, x = 0
        if not filtered_digits:
            return 0
            
        # Form the new integer x by joining the digits
        x = int("".join(filtered_digits))
        
        return x * digit_sum