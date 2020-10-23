class Solution:
    def climbStairs(self, n):
        if n == 1 or n == 0: return 1 if n == 1 else 0
        
        fst, scnd = 1, 1
        
        for i in range(n):
            fst, scnd = scnd, fst + scnd
        return fst