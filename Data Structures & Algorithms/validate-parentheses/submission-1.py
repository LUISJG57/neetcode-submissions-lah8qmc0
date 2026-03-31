class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #creamos un stack el cual servira para luego comparar
        close2open = {')':'(', '}':'{', ']':'['} #creamos un diccionario el cual tiene como clave una llave cerrada y de valor una llave abierta
        for c in s: #para cada caracter en el string
            if c in close2open: #si c es uno de los valores del diccionario (llave cerrada)
                if stack and stack[-1] == close2open[c]:
                #si existe stack y su ultina posicion es igual a su valor ex '( == )' en el dicctionario,
                #la eliminamos del stack 
                    stack.pop()
                else: 
                #en cualquier otro caso '( == ]' pues retornamos falso
                    return False
            else: #sino es una llave abierta la agregamos para que sirva para poder compararla
                stack.append(c)
        # si no existe el stack quiere decir que recorrimos toda la lista y eliminamos todos los parentesis por lo tanto es verdadero, pero si la lista contiene un elemento pues devolveremos falso
        return True if not stack else False

