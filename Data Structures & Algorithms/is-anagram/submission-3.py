from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for i,j in zip(s,t):
            count[i] += 1
            count[j] -= 1
            

        return all(v == 0 for v in count.values())