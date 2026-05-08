class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        #print(nums[0:k])
        l = 0
        while k <= len(nums):
            res.append(max(nums[l:k]))
            l+= 1
            k += 1
        return res

