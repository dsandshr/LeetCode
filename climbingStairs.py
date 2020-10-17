class Solution:
    def climbStairs(self, n):
        if n == 1: return 1
        
        fst = 1
        scnd = 2
        
        for i in range(3, n + 1):
            thrd = fst + scnd
            fst = scnd
            scnd = thrd
        return scnd