class Solution:
    def isValid(self, s: str) -> bool:
        cola = {')': '(', '}':'{', ']':'['}
        res = []

        for c in s:
            if c in cola:
                if res and res[-1] == cola[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        return True if not res else False