class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximo = 0
        cur = 0
        l = 0
        while l < len(nums):
            if nums[l] == 0:
                maximo = max(cur, maximo)
                cur = 0
            else:
                cur += 1
            l+= 1
        maximo = max(cur, maximo)
        return maximo