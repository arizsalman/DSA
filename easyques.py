# # digits = [1,2,3]==>[1,2,4]
# def dig(digits):
#     n = len(digits)
#     for i in range(n-1, -1, -1):
#         if digits[i] < 9:
#             digits[i] += 1
#             return digits
#         digits[i] = 0
#     return [1] + digits

# # [4,3,2,1] 0,1,2,3,=>1,2,3,4 ab  9 = 0 => 1,0 agar ham return me 0 nahe karwte tu requirement puri nahe hote  is leye hum ne 1ko plus kia


# print(dig([9]))
# # print(dig([1, 2, 3]))

# number = [-3, -2, -1, 0, 1, 2, 3, 4, ..., 40]
# number = list(range(41))
# # print(number)
# for i in range(10, -11, -2):
#     print(i)


strs = ["flower", "flow", "flight"]
# Output: "fl"
# st = len(strs)


# def fl(strs):
#     perfix = strs[0]
#     for i in strs[1:]:
#         while not i.startswith(perfix):
#             perfix = perfix[:-1]
#             if not perfix:
#                 return ""
#     return perfix


# print(fl(["flower", "flow", "flight", ]))


# na = ["Ajhgfdftg", "Iuytrf"]
# nb = ["Ajojhvf", "Izsedrtg"]
# st1 = ''.join(na)
# st2 = ''.join(nb)
# common = " ".join([ch for ch in st1 if ch in st2])
# ''' Is method me sab common a gei & data type is string  '''
# print(common)
# print(type(common))


# nam = ["Ajhgfdftg", "Iuytrasief"]
# nab = ["hdIhdauf", "Izselskdpme"]
# str1 = ''.join(nam)
# str2 = ''.join(nam)
# # is ne sab ko ak kerdeya or & data type is dictionary .{a...z}
# comon = set(str1) and set(str2)
# print(comon)
# print(type(comon))


# str2 = ["AirzSalnam", "AliSalman", "AreeshAhmed"]


# def na_call(str2):
#     perfic = str2[0]
#     for word in str2[1:]:
#         while not word.startswith(perfic):
#             perfic = perfic[:-1]
#             if not perfic:
#                 return " alphabet are Not availble  "
#     return perfic


# print(na_call(["ariz", "ali", "aireesh", "aiashir"]))
# print(na_call(["0", "a", "d", "g"]))
nums = [4, 0, 3, 2, 1, 2, 2, 3, 1, 0]
# k = list(set(nums)) #set me takreban random value genrate hote he
# def func(nums):
nums.sort()
# k = sorted(nums)

print(nums)
# print(k)


def func(nums):
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        nums[fast] != nums[slow]
        slow += 1
        nums[slow] = nums[fast]
    return slow+1


print(func([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
