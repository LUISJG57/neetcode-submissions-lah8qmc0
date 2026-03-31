class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set(nums)
        #print(len(nums))
        #print(len(res))
        if len(res) == len(nums):
            return False
        return True