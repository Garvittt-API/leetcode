class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        
        # Collect lengths of contiguous '0' blocks
        zero_blocks = [len(block) for block in s.split('1') if block]
        
        # Find maximum sum of two adjacent '0' blocks
        max_trade_gain = 0
        for i in range(len(zero_blocks) - 1):
            max_trade_gain = max(max_trade_gain, zero_blocks[i] + zero_blocks[i + 1])
            
        return initial_ones + max_trade_gain