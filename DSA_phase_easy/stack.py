
# def func(s):
#     stack = []
#     mapping = {
#         ')': '(',
#         '}': '{',
#         ']': '['
#     }

#     for char in s:
#         if char in mapping:
#             top = stack.pop() if stack else '#'

#             if mapping[char] != top:
#                 return False
#         else:
#             stack.append(char)
#     return not stack


# print(func('()'))
# print(func('(){]}'))

def func(s):
    stack = []
    for i in s:
        if i == '*':
            if stack:
                stack.pop()
        else:
            stack.append(i)

    return ''.join(stack)


print(func(s="leet**cod*e"))
