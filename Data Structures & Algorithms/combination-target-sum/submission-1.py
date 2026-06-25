class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(index, path):
            if sum(path) == target:
                res.append(path[:])
                return
            if index >= len(nums) or sum(path) > target:
                return
            path.append(nums[index])
            backtracking(index, path)
            path.pop()
            backtracking(index+1, path)
        backtracking(0,[])
        return res
