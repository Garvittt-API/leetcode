class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        rev = 0
        # In Python, standard modulo on negative numbers behaves differently than C++/Java,
        # so it's easier to handle the sign up front.
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check for overflow before multiplying
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
                return 0
                
            rev = rev * 10 + pop
            
        return rev * sign