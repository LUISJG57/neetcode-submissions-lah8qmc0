class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        aux = Counter(nums)
        print(aux.values())
        print(aux.keys())
        print(sorted(aux.keys(), key=aux.get, reverse = True))
        return sorted(aux.keys(), key=aux.get, reverse = True)[:k]