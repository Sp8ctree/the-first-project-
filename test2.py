from string import *
res = []
rus_uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
rus_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
slovo = input('Что кодируем?')
sdvig = int(input("Каков сдвиг?"))
for i in slovo:
    if i in ascii_lowercase:res.append(ascii_lowercase[(ascii_lowercase.index(i)+sdvig)%26])
    if i in ascii_uppercase: res.append(ascii_uppercase[(ascii_uppercase.index(i) + sdvig) % 26])
    if i in rus_uppercase:res.append(rus_uppercase[(rus_uppercase.index(i)+sdvig)%26])
    if i in rus_lowercase: res.append(rus_lowercase[(rus_lowercase.index(i) + sdvig) % 26])
    if i in digits: res.append(digits[(digits.index(i) + sdvig) % 10])
print(''.join(res))

