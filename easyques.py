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

number = [-3, -2, -1, 0, 1, 2, 3, 4, ..., 40]
number = list(range(41))
# print(number)
for i in range(10, -11, -2):
    print(i)
    