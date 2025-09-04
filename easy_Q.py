# Leetcode ques no 1

# order = [3, 1, 2, 5, 4], friends = [1, 3, 4]


def func(order, friends):

    n = []

    for i in order:
        if i in friends:
            n.append(i)

    return n


print(func([3, 1, 2, 5, 4], [1, 3, 4]))
