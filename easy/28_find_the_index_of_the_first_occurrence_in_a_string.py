def index_the_first_occurrence(haystack: str, needle: str) -> int:
    """
    Возвращает индекс первого вхождения строки needle в строку haystack
    """
    try:
        return haystack.index(needle)
    except:
        return -1


print(index_the_first_occurrence(haystack="sadbutsad", needle="sad"))
print(index_the_first_occurrence(haystack="leetcode", needle="leeto"))