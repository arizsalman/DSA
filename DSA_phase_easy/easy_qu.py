
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


# q no 88


# nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
# n = 0
# for i in range(len(nums1), -1, -1):
#     if nums1[n] == nums2[i]:
#         nums1[i] = nums2[i]
#         n += 1
# return n

# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# p1 = m-1
# p2 = n-1
# p = m+n-1
# while p2 >= 0:
#     if p1 >= 0 and nums1[p1] > nums2[p2]:
#         nums1[p] = nums1[p1]
#         p1 -= 1
#         print(p1)
#     else:
#         nums1[p] = nums2[p2]
#         p2 -= 1
#     p -= 1
#     print(p)
# print(nums1)


prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]


def func(prices):
    min_price = prices[0]
    max_profite = 0

    for i in range(0, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            profit = prices[i] - min_price
            if profit > max_profite:
                max_profite = profit

    return max_profite


print(func([7, 1, 5, 3, 6, 4]))
