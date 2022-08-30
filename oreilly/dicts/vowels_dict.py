vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Write a word:")
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0) #метод setdefault инициализирует ключ до первого использования
        found[letter] += 1
for k, v in sorted(found.items()):  #sorted - встроенная функция для словарей; метод items позволяет
                                    #организовать итерации по связке ключ-значение (k-v)
    print(k, 'was found', v, 'time(s).')
