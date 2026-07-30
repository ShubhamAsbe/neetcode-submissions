from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d=defaultdict(int)

        if len(s)!=len(t):
            return False
        for i in s:
            d[i]+=1
        for j in t:
            d[j]-=1
            if d[j]<=0:
                del d[j]
        return True if sum(d.values())==0 else False
        