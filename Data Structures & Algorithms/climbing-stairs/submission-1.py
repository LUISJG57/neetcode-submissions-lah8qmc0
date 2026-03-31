class Solution:
    def climbStairs(self, n: int) -> int:
        temp = {}

        def stairs(steps):
            if steps <= 2:
                return steps
            if steps not in temp:
                temp[steps] = stairs(steps - 1) + stairs(steps - 2)
            return temp[steps]
        
        return stairs(n)
