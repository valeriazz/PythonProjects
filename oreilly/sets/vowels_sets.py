word = input("Write a word:")
vowels = set('aeiou')
letters = vowels.intersection(set(word))
print(letters)
