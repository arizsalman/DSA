def func(nums,  target):
    left, right = 0, len(nums)-1
    while left <= right:
        # mid = (left+right) % 2
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1


# print(func([-1, 0, 3, 5, 9, 12], 9))
print(func(nums=[-1, 0, 3, 5, 9, 12], target=9))
