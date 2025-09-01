
# nums = [3, 2, 2, 3], val = 3
# Output: 2, nums = [2,2,_,_]
# nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
#  5, nums = [0,1,4,0,3,_,_,_]


# def func(nums):
#     slow = 0
#     for fast in range(1, len(nums)):
#         if nums[fast] != nums[slow]:
#             slow += 1
#             nums[fast] = nums[slow]
#     return slow
# # 0,1,2,3,4


# print(func([3, 2, 2, 3]))
# print(func([0, 1, 2, 2, 3, 0, 4, 2]))


def remo(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


print(remo(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
print(remo(nums=[3, 2, 2, 3], val=2))
