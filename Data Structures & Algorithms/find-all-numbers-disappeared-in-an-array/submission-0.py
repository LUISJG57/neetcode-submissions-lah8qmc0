class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        aux = [False] * len(nums)
        for num in nums:
            aux[num-1] = True
        print(aux)
        res =[]
        c = 0
        for num in aux:
            c+= 1
            if not num:
                res.append(c)
        return res
