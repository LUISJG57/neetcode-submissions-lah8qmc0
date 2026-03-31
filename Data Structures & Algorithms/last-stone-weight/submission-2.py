class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >1:
            stones.sort()
            tmp = stones.pop() - stones.pop()
            if tmp:
                stones.append(tmp)
        return stones[0] if stones else 0