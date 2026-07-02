class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        # Pre-compute digit values to avoid calling ord() or int() in loops
        digit_map = {str(i): i for i in range(10)}
        
        # Convert strings to lists of actual integer values
        n1 = [digit_map[c] for c in num1]
        n2 = [digit_map[c] for c in num2]
        
        # Array to hold the products of each positional power
        # Maximum length is len(num1) + len(num2)
        res = [0] * (len(n1) + len(n2))
        
        # Reverse to work from least significant digit to most significant
        n1.reverse()
        n2.reverse()
        
        # Multiply positions
        for i, d1 in enumerate(n1):
            for j, d2 in enumerate(n2):
                res[i + j] += d1 * d2
        
        # Carry over the values
        carry = 0
        for i in range(len(res)):
            total = res[i] + carry
            res[i] = total % 10
            carry = total // 10
            
        # Reverse back, remove leading zeros, and join
        while len(res) > 1 and res[-1] == 0:
            res.pop()
            
        res.reverse()
        return "".join(str(d) for d in res)