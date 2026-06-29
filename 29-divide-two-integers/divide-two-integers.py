class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)
        quotient = 0

        while a >= b:
            temp_b, count = b, 1
            while a >= (temp_b << 1):
                temp_b <<= 1
                count <<= 1

            a -= temp_b
            quotient += count
        
        result = -quotient if negative else quotient

        return max(INT_MIN, min(INT_MAX, result))