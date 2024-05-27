def roman_to_integer(roman: str) -> int:
    """
    Первод римских цифр в int
    """
    roman_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    count = 0
    roman = roman.replace("IV", "IIII").replace("IX", "VIIII")
    roman = roman.replace("XL", "XXXX").replace("XC", "LXXXX")
    roman = roman.replace("CD", "CCCC").replace("CM", "DCCCC")
    for i in roman:
        for key, value in roman_int.items():
            if i in key:
                count += value
    return int(count)


print(roman_to_integer(roman="III"))
print(roman_to_integer(roman="LVIII"))
print(roman_to_integer(roman="MCMXCIV"))