class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        good = sorted(heights)
        print(good)
        for i in range(len(heights)):
            if heights[i] != good[i]:
                res += 1
        return res