class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Map characters to their actual integer values
        digit_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        
        # Build the actual numerical value of num1 manually using place values
        n1 = 0
        for char in num1:
            n1 = n1 * 10 + digit_map[char]
            
        # Build the actual numerical value of num2 manually
        n2 = 0
        for char in num2:
            n2 = n2 * 10 + digit_map[char]
            
        # Multiply the two native integers
        product = n1 * n2
        
        # Edge case for zero
        if product == 0:
            return "0"
            
        # Convert the product back to a string manually without str()
        result = []
        while product > 0:
            result.append(chr(ord('0') + (product % 10)))
            product //= 10
            
        return "".join(reversed(result))