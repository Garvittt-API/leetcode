class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        res = "1"
        
        # Generate the sequence iteratively from 2 to n
        for _ in range(n - 1):
            next_res = []
            i = 0
            while i < len(res):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    count += 1
                    i += 1
                # Append count and the character to the list
                next_res.append(str(count))
                next_res.append(res[i])
                i += 1
            # Update result for the next iteration
            res = "".join(next_res)
            
        return res