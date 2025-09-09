# def func(nums,  target):
#     left, right = 0, len(nums)-1
#     while left <= right:
#         # mid = (left+right) % 2
#         mid = (left+right)//2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid+1
#         else:
#             right = mid-1
#     return -1


# # print(func([-1, 0, 3, 5, 9, 12], 9))
# print(func(nums=[-1, 0, 3, 5, 9, 12], target=9))


# def func(nums):

#     left, right = 0, len(nums)-1
#     while left < right:
#         mid = (left+right)//2
#         if nums[mid] < nums[mid+1]:
#             left = mid+1
#         else:
#             right = mid-1

#     return left


# print(func([1, 2, 3, 1]))


# question no 34
# nums = [5, 7, 7, 8, 8, 10], target = 8
# Output = [3, 4]
# nums = [5, 7, 7, 8, 8, 10], target = 6
# Output = [-1, -1]


# def func(nums, target):

#     def firstfunc(nums, target):
#         left, right = 0, len(nums)-1
#         first = -1
#         while left <= right:
#             mid = (left + right)//2
#             if nums[mid] == target:
#                 first = mid
#                 right = mid - 1
#             else:
#                 if nums[mid] < target:
#                     left = mid+1
#                 else:
#                     right = mid-1
#         return first

#     def lastfunc(nums, target):
#         left, right = 0, len(nums)-1
#         last = -1
#         while left <= right:
#             mid = (left+right)//2
#             if nums[mid] == target:
#                 last = mid
#                 left = mid+1
#             else:
#                 if nums[mid] < target:
#                     left = mid+1
#                 else:
#                     right = mid-1
#         return last
#     return [firstfunc(nums, target), lastfunc(nums, target)]


# print(func([5, 7, 7, 8, 8, 10], 8))


# def func(letters, target):
#     n = len(letters)
#     left, right = 0, n
#     while left < right:
#         mid = (left + right)//2
#         if letters[mid] == target:
#             return mid
#         else:
#             if letters[mid] <= target:
#                 left = mid+1
#             else:
#                 right = mid
#     return letters[left % n]


# print(func(["c", "d", "f"], "a"))
# print(func(letters=["c", "f", "j"], target="c"))

"""ye Rotated array he is me hum normal tarake se nahe hum phele half  left side check kar ge agar us me mel gaya sahe or agar nahe mala tu hum right side ko check kare ge .. is leye rotated me normal tarke se used nahe karte  """


def func(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if nums[mid] < target <= right:
                left = mid+1
            else:
                right = -1

    return -1


print(func(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
