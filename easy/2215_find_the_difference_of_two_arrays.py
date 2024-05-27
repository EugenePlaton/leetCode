# Более быстрый и менее затратный по памяти вариант
def difference_between_two_arrays(nums1: list, nums2: list) -> list:
    """
    Возвращает разницу между двумя списками.
    В первом списке возвращаем все целые числа из nums1, которых нет в nums2
    Во втором списке возвращаем все целые числа из nums2, которых нет в nums1
    """
    nums1 = set(nums1)
    nums2 = set(nums2)
    return [list(nums1 - nums2), list(nums2 - nums1)]

# Первый вариант реализации
# def difference_between_two_arrays(nums1: list, nums2: list) -> list:
#     res1 = list({num for num in nums1 if nums2.count(num) <= 0})
#     res2 = list({num for num in nums2 if nums1.count(num) <= 0})
#     return [res1, res2]


print(difference_between_two_arrays(nums1=[1, 2, 3], nums2=[2, 4, 6]))
print(difference_between_two_arrays(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))
