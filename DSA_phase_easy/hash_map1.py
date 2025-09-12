def func(s, t):
    hash_map = {}
    for i in s:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1

    for i in t:
        hash_map[i] -= 1

    for i in hash_map:
        if hash_map[i] > 0:
            return i


print(func("abbc", "abb"))
print(func("abbe", "abb"))
