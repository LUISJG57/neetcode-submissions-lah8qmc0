class MinStack:
    def __init__(self):
        #creamos dos pilas una en donde se iran los valores 
        self.stack = [] #valores predeterminados
        self.minStack = [] #valor minimo

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) #Si minStack está vacío, el valor val se convierte automáticamente en el mínimo actual.
        self.minStack.append(val) #Almacena el mínimo actual en la pila de mínimos (minStack).

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]