def search_for_vowels(word):
    """Возвращает булево значение в зависимости от присутствия любых гласных."""
    vowels = set('aeiou')
    found = sorted(vowels.intersection(set(word)))
    return bool(found)


search_for_vowels('Lerushka')


def search_for_vowels(phrase: str) -> set:
    """Возвращает найденные в слове гласные."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


search_for_vowels('Lerushka')