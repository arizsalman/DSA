nums = [4, 3, 10, 9, 8]

# nums.sort()
# print(nums)
# res = []
# while sum(res) <= sum(nums):
#     res.append(nums.pop())
#     print(res)

# nums = [4, 3, 10, 9, 8]
# nums.sort(reverse=True)
# total = sum(nums)
# print(total)
# subseq = []
# cuur_sum = 0
# for n in nums:
#     subseq.append(n)
#     cuur_sum += n
#     print(f'Step: {subseq} Sum : {cuur_sum}')
#     if cuur_sum > total-cuur_sum:
#         break
#     # print(subseq)

# [10,9]

# numz = [4, 3, 10, 9, 8]
# # output [10,9]
# numz.sort(reverse=True)
# total = sum(numz)
# print(f' num{numz}; sum {total}')
# sub = []
# run = 0
# for i in numz:
#     sub.append(i)
#     # print(f' my i is {i} ; numz is {numz}')
#     run += i
#     print(run)
#     if run > total-run:
#         break
#     print(f'the value is here {sub}')

# print(f' final list is upgrade :{sub}')


numh = [4, 3, 10, 9, 8]
# output=[10,9]
numh.sort(reverse=True)
total = sum(numh)

serq = []
count = 0
for x in numh:
    serq.append(x)
    count += x
    if count > total-count:
        break
print(serq)
