class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        aux = set()
        for num in nums:
            if num in aux:
                return num
            aux.add(num)
        return -1