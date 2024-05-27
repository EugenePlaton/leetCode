def detect_capital(word: str) -> bool:
    """
    Возвращает верно ли использование заглавных букв в слове. Верные утверждения:
    Все буквы в этом слове заглавные, например "USA".
    Все буквы в этом слове не заглавные, например "leetcode".
    Только первая буква в этом слове заглавная, например "Google".
    """
    return word.isupper() or word.islower() or word.capitalize() == word


print(detect_capital(word="USA"))
print(detect_capital(word="FlaG"))