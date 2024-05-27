def majority_element(nums):
    """
    Возвращает majority element - элемент, который
    встречается в списке больше раз, чем n / 2
    """
    return next(iter(list(num for num in set(nums) if nums.count(num) > len(nums) / 2)))


print(majority_element([3,2,3]))
print(majority_element([2,2,1,1,1,2,2]))