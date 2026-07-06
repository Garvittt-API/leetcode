class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        # Sort by start ascending, then by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining_count = 0
        max_end = 0
        
        for start, end in intervals:
            # If the current interval's end fits within the max_end seen so far,
            # it is completely covered because start >= previous_start.
            if end > max_end:
                remaining_count += 1
                max_end = end
                
        return remaining_count