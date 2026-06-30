from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            # groupby automatically collects consecutive identical characters
            # e.g., "33222" -> ('3', iter(['3', '3'])), ('2', iter(['2', '2', '2']))
            res = "".join(str(len(list(group))) + digit for digit, group in groupby(res))
        return res