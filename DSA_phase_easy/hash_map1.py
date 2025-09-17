# def func(s, t):
#     hash_map = {}
#     for i in s:
#         if i in hash_map:
#             hash_map[i] += 1
#         else:
#             hash_map[i] = 1

#     for i in t:
#         hash_map[i] -= 1

#     for i in hash_map:
#         if hash_map[i] > 0:
#             return i


# print(func("abbc", "abb"))
# print(func("abbe", "abb"))

# leet no 350
def func(nums1, nums2):
    hash_map = {}
    result = []
    for i in nums2:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1

    for j in nums1:
        if j in hash_map and hash_map[j] > 0:
            result.append(j)
            hash_map[j] -= 1
    return result


print(func([1, 2, 2, 1], [2, 2]))

# [3, 2, 3]


def func(nums):
    hash_map = {}
    for i in nums:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    n = len(nums)
    for i in hash_map:
        if hash_map[i] > n//2:
           return i


print(func([3, 2, 3]))

# nums1 = [1,2,2,1], nums2 = [2,2]


def func(nums1, nums2):
    hash_map = {}
    result = []
    for i in nums1:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    for j in nums2:
        if j in hash_map:
            result.append(j)
            del hash_map[j]
    return result


print(func(nums1=[1, 2, 2, 1], nums2=[2, 2]))
