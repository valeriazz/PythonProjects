word = input()
vowels = ['a', 'e', 'i', 'o', 'u']
list = []
for i in word:
    if i in vowels and i not in list:
        list.append(i)
print(*list)