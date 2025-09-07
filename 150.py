from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []

    for t in tokens:
        if t in "+-/*":
            snd = stack.pop()
            fst = stack.pop()

            if t == "+":
                stack.append(fst + snd)
            elif t == "-":
                stack.append(fst - snd)
            elif t == "/":
                stack.append(fst / snd)
            else:
                stack.append(fst * snd)
        else:
            stack.append(t)

    return stack[0]
