from string import *
res = []
slovo = input('Что кодируем?')
sdvig = int(input("Каков сдвиг?"))
for i in slovo:
    if i in ascii_uppercase:res.append(ascii_uppercase[(slovo.index(i) + sdvig)%(len(ascii_uppercase)-1)])
    if i in ascii_lowercase:res.append(ascii_lowercase[(slovo.index(i) + sdvig)%(len(ascii_lowercase)-1)])
    if i in digits:res.append((digits[(slovo.index(i) + sdvig+1)%(len(digits))]))
print(''.join(res))
