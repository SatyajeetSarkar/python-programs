''' Postfix evaluation '''

def evaluate_postfix(expression):
    stack = []

    tokens = expression.split()

    for token in tokens:

        if token.isdigit():
            stack.append(int(token))

        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)

            elif token == '-':
                stack.append(a - b)

            elif token == '*':
                stack.append(a * b)

            elif token == '/':
                stack.append(a / b)

            elif token == '%':
                stack.append(a % b)

    return stack.pop()


postfix = "5 6 2 + * 12 4 / -"
result = evaluate_postfix(postfix)

print(postfix)
print("Result:", result)