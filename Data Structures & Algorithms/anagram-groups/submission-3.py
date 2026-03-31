class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 # count = 0000...26 hasta 26 ceros que representa el abc
            for c in s: 
                count[ord(c) - ord("a")] += 1 #le damos un valor unico a cada string con su valor ASCII
                #y cada que salga aumentamos el contador
            #despues de completar toda la palabra la agregamos en su index 
            res[tuple(count)].append(s) #usamos tuple para crear lista
        #regresamos los valores asignados de todas las listas
        return res.values()