from string import*
a=[]
s=ascii_lowercase+'a'
q=str(input('введите слово'))
y=int(input('введите число сдвига'))

b=[]
for i in q:
    for i2 in s:
        if i==i2:
            b.append(s.index(i2)+y)

for x in b:
    a.append(s[x])
print(q,'-ваше слово')
print(''.join(str(t)for t in a),'-закодированное слово')