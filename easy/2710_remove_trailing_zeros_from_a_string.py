def remove_zeroes_at_end(num: str) -> str:
    """
    Удаляет нули в конце строки
    """
    while num[-1] == '0':
        num = num[:-1]
    return num


print(remove_zeroes_at_end(num="51230100"))
print(remove_zeroes_at_end(num="123"))

