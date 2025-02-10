def simplify_path(s):
    s = s.split('/')
    stack = []

    for i in range(len(s)):
        if s[i] == '' or s[i] == '.':
            continue
        elif s[i] == '..':
            if stack:
                stack.pop()
        else:
            stack.append(s[i])

    return '/' + '/'.join(stack)


print(simplify_path("/home/user/Documents/../Pictures"))
print(simplify_path("/.../a/../b/c/../d/./"))
print(simplify_path("/home/"))
print(simplify_path("/../"))
