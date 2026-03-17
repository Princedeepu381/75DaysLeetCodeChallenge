from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # most_common(k) returns a list of tuples: [(num, count), ...]
        return [num for num, count in Counter(nums).most_common(k)]