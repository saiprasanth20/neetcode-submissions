class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their ending time
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # Overlapping interval -> remove it
                removals += 1
            else:
                # Non-overlapping -> keep it
                prev_end = end

        return removals