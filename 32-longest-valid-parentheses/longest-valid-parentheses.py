class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # New base for valid substrings
                    stack.append(i)
                else:
                    # Calculate length of current valid match
                    max_len = max(max_len, i - stack[-1])
        
        return max_len