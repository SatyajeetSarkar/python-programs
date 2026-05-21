''' Infix to Postfix using Stack '''

def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:

        if ch.isalnum():
            postfix += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   precedence(ch) <= precedence(stack[-1])):
                postfix += stack.pop()

            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix


infix = "A+B*(C-D)"
postfix = infix_to_postfix(infix)

print("Infix Expression :", infix)
print("Postfix Expression:", postfix)