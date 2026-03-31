class Solution:
    def aux(self, n):
        cnt = 0
        while n:
            digit = n%10
            digit = digit**2
            cnt += digit
            n = n//10
        return cnt
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n and n not in visit:
            visit.add(n)
            n = self.aux(n)
            if n== 1:
                return True
        return False
    