class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        maximo = -1
        for i in range(len(arr)-1,-1,-1):
            print(arr[i])
            res[i] = maximo
            maximo = max(maximo, arr[i])
        return res