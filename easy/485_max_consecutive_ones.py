def max_consecutive_ones(nums: list) -> int:
    """
    Возвращает максимальное количество последовательных 1 в массиве
    """
    res = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            res = max(res, count)
            count = 0
    return max(res, count)


print(max_consecutive_ones(nums=[1, 1, 0, 1, 1, 1]))
print(max_consecutive_ones(nums=[1, 0, 1, 1, 0, 1]))