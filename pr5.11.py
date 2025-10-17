s = input('Введите строку: ')
pn = 0
mx = 0
for n in range(0, len(s)):
    if s[n]=='н':
        pn += 1
        mx = max(mx, pn)
    else:
        pn = 0
s = s.replace('!', '.')
print(mx, s)
