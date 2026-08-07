import heapq
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = defaultdict(int)

        for num in nums:
            d[num] += 1

        priority_queue = []

        for num, freq in d.items():

            if len(priority_queue) < k:
                heapq.heappush(priority_queue, (freq, num))

            elif freq > priority_queue[0][0]:
                heapq.heappop(priority_queue)
                heapq.heappush(priority_queue, (freq, num))

        return [num for freq, num in priority_queue]