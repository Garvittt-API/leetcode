class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the negative exponent case
        if n < 0:
            x = 1 / x
            n = -n
            
        result = 1.0
        current_product = x
        
        while n > 0:
            # If n is odd, multiply the current_product with the result
            if n % 2 == 1:
                result *= current_product
            
            # Square the base and divide the exponent by 2
            current_product *= current_product
            n //= 2
            
        return result