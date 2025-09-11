# nums = [2,2,3,2]
# def func(nums):
#     hash_map = {}
#     for check in nums:
#         if check in hash_map:
#             hash_map[check] += 1
#         else:
#             hash_map[check] = 1
#     for checks in hash_map:
#         if hash_map[checks] != 3:
#             return checks


# print(func([2, 2, 3, 2]))


# s = "anagram", t = "nagaram"


# def func(s, t):
#     hash_map = {}
#     for check, val in zip(s, t):
#         if check in val:
#             hash_map = check
#             return True
#         else:
#             False
#     return hash_map

""" this is Wrong method """
# print(func(s="anagram", t="nagaram"))


# def func(s, t):
#     if len(s) != len(t):
#         return False
#     else:
#         return sorted(s) == sorted(t)


# print(func(s="anagram", t="nagaram"))

"""Question no 242 ^ same in simple  | neje vala same HashMap used"""
# def func(s, t):
#     if len(s) != len(t):
#         return False
#     hash_map = {}
#     for i in s:
#         if i in hash_map:
#             hash_map[i] += 1
#         else:
#             hash_map[i] = 1
#     for y in t:
#         if y not in hash_map:
#             return False
#         elif hash_map[y] == 1:
#             del hash_map[y]
#         else:
#             hash_map[y] -= 1
#     return True


# print(func(s="anagram", t="nagaram"))


"""Question no 383 """
# ransomNote = "aa", magazine = "aab"


def func(ransomNote, magazine):
    hash_map = {}
    for i in magazine:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    for y in ransomNote:
        if y not in hash_map:
            return False
        elif hash_map[y] == 1:
            del hash_map[y]
        else:
            hash_map[y] -= 1
    return True


print(func(ransomNote="aa", magazine="aab"))
