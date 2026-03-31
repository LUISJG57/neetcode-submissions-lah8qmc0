class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #creamos un hashmap el cual nos servira para comparar
        #usamos enumerate porque ocupamos buscar indice y su valor
        for i, n in enumerate(nums): 
            #variable de diferencia en este caso imaginemso t = 7 n = 3, entonces 7-3 = 4
            diff = target - n
            if diff in prevMap: #si el valor que necesitamos de la diferencia se encuentra
            #en nuestro prevMap devolveremos el indice de nuestra iteracion actual junto con el indice de la diferencia
                return [prevMap[diff], i]
            prevMap[n]= i #en cualquier otro caso guardaremos el valor en nuestro mapa