class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == s:
            return s
        t = list(t)
        res = ""
        l = 0
        r = 0
        while l < len(s):
            if s[l] in t:
                r = l+1
                tCopy = t.copy()
                #print(tCopy)
                tCopy.remove(s[l])
                if not tCopy:
                        current = s[l:r]
                        if res == "" or len(current) < len(res):
                            res = current
                while r < len(s):
                    if s[r] in tCopy:
                        tCopy.remove(s[r])
                    r += 1
                    if not tCopy:
                        current = s[l:r]
                        if res == "" or len(current) < len(res):
                            res = current
                        break
            l += 1
        return res
