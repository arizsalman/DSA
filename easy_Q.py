# Leetcode ques no 1

# order = [3, 1, 2, 5, 4], friends = [1, 3, 4]


# def func(order, friends):

#     n = []

#     for i in order:
#         if i in friends:
#             n.append(i)

#     return n


# print(func([3, 1, 2
# , 5, 4], [1, 3, 4]))


# def func(nums):
#     seen = set()
#     for i in nums:
#         if i in seen:
#             return True
#         seen.add(i)
#     return False


# print(func(nums=[1, 2, 3, 1]))


# def func(nums):
#     seem = set()
#     for i in nums:
#         if i in seem:
#             return True
#         else:
#             seem.add(i)
#     return False


# print(func([1, 2, 3, 4, 5, 6, 7, 0]))
# print(func([1,  2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1]))


def func(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    '''Kyoki closing bracket aate hi check karna hota hai uska matching opening bracket stack ke top pe hai ya nahi, isliye mapping me keys hamesha closing brackets hote hain. ✅'''
    for char in s:
        if char in mapping:
            print(f' d stack {stack}')
            top = stack.pop() if stack else '#'
            print(f' is stack : {stack}')
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack


print(func("([])"))
# print(func("({{}])"))        # True
# print(func("()[]{}"))    # True
# print(func("{[]}"))      # True
