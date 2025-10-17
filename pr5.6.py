s = input('Введите строку: ')
k = 0
a = []
for i in range(0, len(s)):
    if s[i]=='a':
        k += 1
    else:
        a.append(s[i])
print(k, a)
