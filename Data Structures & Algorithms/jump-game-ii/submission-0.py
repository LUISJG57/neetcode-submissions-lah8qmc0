class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        aux = 0
        while r < len(nums)-1:
            lejos = 0
            for i in range(l, r+1):
                lejos = max(lejos, i + nums[i])
            l = r+1
            r = lejos
            aux+=1 
        return aux