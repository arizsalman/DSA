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


def func(nums, target):

    def firstfunc(nums, target):
        left, right = 0, len(nums)-1
        first = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                first = mid
                right = mid - 1
            else:
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
        return first

    def lastfunc(nums, target):
        left, right = 0, len(nums)-1
        last = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                last = mid
                left = mid+1
            else:
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
        return last
    return [firstfunc(nums, target), lastfunc(nums, target)]


print(func([5, 7, 7, 8, 8, 10], 8))
