class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        curr = n
        while True:
            product = 1 
            temp = curr
            while temp > 0: 
                product *= temp % 10
                temp //= 10

            if product % t == 0:
                return curr

            curr += 1