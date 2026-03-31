class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        aux = nums1 + nums2
        aux.sort()
        print(aux)
        print(len(aux))

        if len(aux) % 2 == 0:
            return (aux[len(aux)// 2 - 1] + aux[len(aux)// 2]) / 2
        else:
            return aux[len(aux)// 2]