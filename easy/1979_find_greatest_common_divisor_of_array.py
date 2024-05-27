def find_greatest_divisor(nums: list) -> int:
    """
    Находит наибольший общий делитель для наибольшего и наименьшего значения списка
    Перебираем все делители, которые меньше минимального числа, в обратном порядке
    и ищем общий для этих значений делитель
    :param nums:
    :return:
    """
    min_value, max_value = min(nums), max(nums)
    for i in range(min_value, 0, -1):
        if min_value % i == 0 and max_value % i == 0:
            return i
