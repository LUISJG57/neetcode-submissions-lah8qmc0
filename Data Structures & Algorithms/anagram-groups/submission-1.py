class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 

        for s in strs: #para cada string en el grupo de strings
            count = [0] * 26 #esto sirve para guardar cuantas veces se uso una letra, en este caso con el abecedario hay 26 caracteres

            for c in s: #para cada caracter en uno de los strings
                count[ord(c) - ord("a")] += 1  #basicamente para cada caracter vamos a sacar su valor en ASCII y se lo restaremos al valor ASCII 
                #de "a" de tal manera que obtendremos un numero al cual poder asignar en el hash (ex si a= 10 y b= 11, su valor con el que guardaremos sera 1 porque 10 - 11)
                # y al final incrementaremos el valor en el hashmap por cada vez que encontremos un numero
            
            # entregamos los key values de cada una de las veces que se uso un caracter 
            res[tuple(count)].append(s)
        
        # entregamos los valores finales
        return res.values()