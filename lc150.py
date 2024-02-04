def evalRPN(tokens):
    stack = []
    for i in tokens:
        print(stack)
        if i == '+':
            stack.append(stack.pop()+stack.pop())
        elif i == '-':
            stack.append(-stack.pop()+stack.pop())
        elif i == '*':
            stack.append(stack.pop()*stack.pop())
        elif i == '/':
            second = stack.pop()
            first = stack.pop()
            stack.append(int(first/second))
        else:
            stack.append(int(i))
    return stack[0]

print(evalRPN(tokens = ["2","1","+","3","*"]))