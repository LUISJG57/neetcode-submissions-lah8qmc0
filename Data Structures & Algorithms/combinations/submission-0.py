class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtracking(i, path):
            if i > n:
                if len(path) == k:
                    res.append(path[:])
                return
            path.append(i)
            backtracking(i+1, path)
            path.pop()
            backtracking(i+1, path)
        backtracking(1,[])
        return res