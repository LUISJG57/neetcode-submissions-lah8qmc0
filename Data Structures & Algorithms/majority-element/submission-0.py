class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        res = 0
        maxC = 0

        for num in nums:
            counter[num] += 1
            if maxC < counter[num]:
                res = num
                maxC = counter[num]
        return res