class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split()
        #print(res[-1])
        return len(res[-1])