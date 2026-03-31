class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1= sorted(s)
        res2= sorted(t)
        if res1 == res2:
            return True
        return False