class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        for v in t:
            if p >= len(s):
                break
            if v == s[p]:
                p += 1
        
        return p >= len(s)
