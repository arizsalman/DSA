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


# def func(ransomNote, magazine):
#     hash_map = {}
#     for i in magazine:
#         if i in hash_map:
#             hash_map[i] += 1
#         else:
#             hash_map[i] = 1
#     for y in ransomNote:
#         if y not in hash_map:
#             return False
#         elif hash_map[y] == 1:
#             del hash_map[y]
#         else:
#             hash_map[y] -= 1
#     return True


# print(func(ransomNote="aa", magazine="aab"))


# 3227 no

# def func(s):
#     vo = set('aeiou')
#     for i in s:
#         if i in vo:
#             return True
#     return False


# print(func('Asjfi'))
# print(func('zjf'))


# leetcode no 387


# s = "leetcode"

# def func(s):
#     hash_map = {}
#     for i in s:
#         if i in hash_map:
#             hash_map[i] += 1
#         else:
#             hash_map[i] = 1
#     for y in hash_map:
#         if hash_map[y] == 1:
#             return y
#     return -1
"""ye method sahe he  but ye index nahe pata raha ye value bata raha he  """

# print(func(s="leetcode"))


def func(s):
    hash_map = {}
    for i in s:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    for y in range(len(s)):
        if hash_map[s[y]]:
            return y
    return -1


"""ye vlaue ka index  bata raha he agar without enumerate loop me index find karn aho tu [s >ye jis pe loop laga he [y>jo s value de raha he y ko ] ] -->[s[y]] ise index find karte he """
print(func(s="leetcode"))


