class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        
        quotient = 0

        powers = []
        val = b
        while val <= a:
            powers.append(val)
            val <<= 1

        for i in range(len(powers) - 1, -1, -1):
            if a >= powers[i]:
                a -= powers[i]
                quotient += (1 << i)
        
        result = -quotient if negative else quotient

        return max(INT_MIN, min(INT_MAX, result))