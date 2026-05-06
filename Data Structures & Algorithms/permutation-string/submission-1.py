class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        map1 = sorted(s1)
        print(map1)
        #map2 = sorted(s2[2:5])
        #print(map2)
        #print(s2[2:5])
        for i in range(len(s2)):
            if sorted(s2[i:i+n]) == map1:
                return True
        return False            
            