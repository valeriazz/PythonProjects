 -*- coding: cp1251 -*-

word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
    print()


# �� ������� �����
word = "�������"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "���� �� �����." )
    print(beer_num, word, "����!")
    print("������ ����.")
    print("����� �� �����.")
    if beer_num == 1:
        print("��� ������� ���� �� �����!")
    else:
        new_num = beer_num - 1
        if new_num >= 11 and new_num <= 19:
            word = "�������"
        else:
            if new_num % 10 == 1:
                word = "�������"
            elif new_num % 10 in (2, 3, 4):
                word = "�������"
            else:
                word = "�������"
    print()

