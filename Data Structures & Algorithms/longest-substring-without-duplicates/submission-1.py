class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,ctr = 0, 0
        res = set()
        while l < len(s):
            
            if s[l] in res:
                res.clear()
                l += 1
                
            else:
                
                res.add(s[l])
                l += 1
            
        return len(res)

        