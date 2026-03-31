class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        print(res)
        for string in strs:
            aux = ''.join(sorted(string))
            res[aux].append(string)
        print(res)
        print(res.values())
        return list(res.values())

