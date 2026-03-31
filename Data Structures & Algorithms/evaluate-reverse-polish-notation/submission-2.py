class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:                
            if c == '+':
                stack.append(stack.pop() + stack.pop())
                print(stack)
            elif c == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a = stack.pop()
                b = stack.pop()
                print('b', b)
                stack.append(int(float(b) / a))
            else: 
                stack.append(int(c))
        print(stack)
        return stack[0]