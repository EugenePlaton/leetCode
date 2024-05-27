def check_digit_count_and_digit_value(num: str) -> bool:
    """
    Дана строка num длины n, состоящая из цифр.
    Возвращет true, если для каждого индекса i цифра i встречается num[i]
    раз в num, иначе верните false.
    """
    res = [(index, key) for index, key in enumerate(num)]
    return all(int(num[index]) == num.count(str(index)) for index, _ in res)


print(check_digit_count_and_digit_value(num="1210"))
print(check_digit_count_and_digit_value(num="030"))
