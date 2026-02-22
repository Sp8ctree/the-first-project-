from string import *
res = []
slovo = input('Что кодируем?')
sdvig = int(input("Каков сдвиг?"))
for i in slovo:
    res.append(ascii_lowercase[slovo.index(i)+sdvig])
print(''.join(res))
