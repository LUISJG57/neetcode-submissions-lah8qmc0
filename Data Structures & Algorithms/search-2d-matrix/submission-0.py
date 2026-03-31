class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for List in matrix:
            for List in List:
                res.append(List)

        L = 0
        R = len(res) - 1
        
        while L <= R:
            mid = (L+R) // 2
            if target > res[mid]:
                L = mid + 1
            elif target < res[mid]:
                R = mid - 1
            else:
                return True
        return False