def moves_zeroes(nums: list) -> list:
    for i in nums:
        if i == 0:
            index = nums.index(i)
            del nums[index]
            nums.append(i)
    return nums


print(moves_zeroes(nums=[0, 1, 0, 3, 12]))
print(moves_zeroes(nums=[0]))