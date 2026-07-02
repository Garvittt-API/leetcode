class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case for zero
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array with zeros
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Loop backwards through both strings
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply digits
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Positions in the result array
                p1 = i + j
                p2 = i + j + 1
                
                # Add product to the current position (handling previous carry)
                total = mul + result[p2]
                
                # Update positions
                result[p2] = total % 10
                result[p1] += total // 10
        
        # Skip leading zero if it exists
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
            
        # Convert digit list back to string
        return "".join(map(str, result[start:]))