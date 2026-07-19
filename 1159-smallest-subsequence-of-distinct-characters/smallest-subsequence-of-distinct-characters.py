class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Record the last index each character appears
        last_occurrence = {c: i for i, c in enumerate(s)}
        
        stack = []
        seen = set()
        
        for i, c in enumerate(s):
            # Skip if the character is already part of our result
            if c in seen:
                continue
            
            # Pop characters from stack if they are larger than current character
            # AND they appear later in the string
            while stack and stack[-1] > c and last_occurrence[stack[-1]] > i:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            stack.append(c)
            seen.add(c)
            
        return "".join(stack)