class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cola = set(nums)
        if len(nums) != len(cola):
            return True
        return False 