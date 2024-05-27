def add_to_array_form_integer(num: list, k: int):
    """
    Возвращает форму массива целого числа num + k.
    Например, для num = 1321 форма массива будет [1,3,2,1].
    """
    num_str = ''.join(str(e) for e in num)
    res = int(num_str) + k
    return [int(x) for x in str(res)]


print(add_to_array_form_integer(num=[1, 2, 0, 0], k=34))
print(add_to_array_form_integer(num=[2, 7, 4], k=181))
print(add_to_array_form_integer(num=[2, 1, 5], k=806))
