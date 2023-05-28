class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1,n):
            if s[i] != s[i-1]:
                ans += min(i,n-i)
        return ans
            
        




