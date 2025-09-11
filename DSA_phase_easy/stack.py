
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
#    Question no 2390 romeoving star
# def func(s):
#     stack = []
#     for i in s:
#         if i == '*':
#             if stack:
#                 stack.pop()
#         else:
#             stack.append(i)

#     return ''.join(stack)


# print(func(s="leet**cod*e"))

# Question no 1047
# s = "abbaca"
# def func(s):
#     stack = []
#     for i in s:
#         if stack and stack[-1] == i:
#             stack.pop()

#         else:
#             stack.append(i)
#     return stack


# print(func('abbaca'))


# s = "ab#c", t = "ad#c"
# def main_func(string):
#     stack = []
#     for check in string:
#         if check in "#":
#             if stack:
#                 stack.pop()
#         else:
#             stack.append(check)
#     return stack


# def func(s, t):
#     return main_func(s) == main_func(t)


# print(func(s='ab##', t='c#d#'))


# Question no 682

# ["5","2","C","D","+"] ops

# def func(operation):
#     stack = []
#     for check in operation:
#         if check == "C":
#             stack.pop()
#         elif check == "D":
#             stack.append(2*stack[-1])
#         elif check == "+":
#             stack.append(stack[-1]+stack[-2])
#         else:
#             stack.append(int(check))

#     return sum(stack)


# print(func(["5", "2", "C", "D", "+"]))


# Question no 225. Implement Stack using Queues [null, null, null, 2, 2, false]
# print(func(["MyStack", "push", "push", "top", "pop", "empty"]))
def func(input):
    stack = []
    result = []
    for check in input:
        if check == "MyStack":
            result.append(None)
        elif check == "push":
            stack.append(2)
            result.append(None)
        elif check == "pop":
            if stack:
                result.append(stack.pop())
            else:
                result.append(None)

        elif check == "top":
            if stack:
                result.append(stack[-1])
            else:
                result.append(None)
        elif check == "empty":
            result.append(len(stack) == 0)
    return result


""" Leetcode Not Accepted """
print(func(["MyStack", "push", "push", "top", "pop", "empty"]))
# print(func(["MyStack", "push", "push", "top", "pop", "empty"]))


def func(commands, values):
    stack = []
    result = []

    for cmd, val in zip(commands, values):
        if cmd == "MyStack":
            stack = []               # naya stack banao
            result.append(None)
        elif cmd == "push":
            stack.append(val[0])     # push value
            result.append(None)
        elif cmd == "pop":
            result.append(stack.pop()) if stack else result.append(None)
        elif cmd == "top":
            result.append(stack[-1]) if stack else result.append(None)
        elif cmd == "empty":
            result.append(len(stack) == 0)
    return result



print(func(
    ["MyStack", "push", "push", "top", "pop", "empty"],
    [[], [1], [2], [], [], []]
))
