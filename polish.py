def to_infix(tokens: list) -> str:
    token = tokens.pop(0)

    if '0' <= token[-1] <= '9':
        return token
    else:
        a = to_infix(tokens)
        b = to_infix(tokens)

        result = a + ' ' + token + ' ' + b
        if token in ('+', '-'):
            result = '(' + result + ')'
        return result

def evaluate(tokens: list) -> float:
    token = tokens.pop(0)

    if '0' <= token[-1] <= '9':
        return float(token)
    else:
        a = evaluate(tokens)
        b = evaluate(tokens)

        if token == '+': return a + b
        elif token == '-': return a - b
        elif token == '*': return a * b
        elif token == '/': return a / b;
        elif token == 'div': return int(a) // int(b)
        elif token == 'mod': return int(a) % int(b)

if __name__ == '__main__':
    polish = '+ * 3 4 * 5 -3'.split()

    infix = to_infix(polish[:])
    value = evaluate(polish[:])
    print(infix, '==', value)
