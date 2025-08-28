# nums = [4, 3, 10, 9, 8]

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


# numh = [4, 3, 10, 9, 8]
# nuz = numh[2: 4]
# print(nuz)
# # output=[10,9]
# numh.sort(reverse=True)
# total = sum(numh)
# serq = []
# count = 0
# for x in numh:
#     serq.append(x)
#     count += x
#     if count > total-count:
#         break
# print(serq)


# nums1 = [2, 5, 7, 3]
# run1 = 0
# current = 0  # current=zero ye dono barabar he
# for i in nums1:
#     print(f' \nthis is i:{i}')
#     current = i
#     run1 += i
#     print(f'\n run1+=i:{run1} and Current = i : {current}')


# num_M = [2, 5, 7, 3]
# mul = 1

# for i in num_M:
#     mul *= i
#     print(mul)


# numbers = [2, 7, 11, 15]
# nuzr = numbers[1:-1]
# print(nuzr)
# indexs = [numbers.index(val) for val in nuzr]
# print(indexs)

'''leetcode Question no 167  =numbers = [2,7,11,15] output =[1,2]'''

numbers = [2, 7, 11, 15]
# output =[1,2]


def twoSum(numbers, target):
    seem = {}
    for i, num in enumerate(numbers):
        complete = target-num
        if complete in seem:
            return [seem[complete]+1, i+1]
        seem[num] = i


print(twoSum([2, 7, 11, 15], 9))


# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
def sum(nums):
    sets = []
    for i in nums:
        # print(i)
        count = 0
        for j in nums:
            # print(j)
            if j < i:
                count += 1
                # print(f'count is {count}')
        sets.append(count)
    return sets


print(sum(nums=[8, 1, 2, 2, 3]))
