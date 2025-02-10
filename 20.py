def valid_brackets(s):
    stack = []
    map = {')': '(', ']': '[', '}': '{'}

    for i in range(len(s)):
        if s[i] in '({[':
            stack.append(s[i])
        else:
            if stack and stack[-1] == map[s[i]]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(valid_brackets('()[]{}'))  # True
