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


def func(nums):
    seem = set()
    for i in nums:
        if i in seem:
            return True
        else:
            seem.add(i)
    return False


print(func([1, 2, 3, 4, 5, 6, 7, 0]))
print(func([1,  2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1]))
