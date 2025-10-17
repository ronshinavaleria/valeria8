b = int(input('Введите длину массива: '))
a = []
for c in range(1, b+1):
    print('Введите', c, 'элемент')
    a.append(int(input()))
m = max(a)
kmen = 0
kbol = 0
for i in range(0, len(a)):
    if a[i]>m:
        kbol += 1
    elif a[i]<m:
        kmen += 1
print('количество меньших максимального: ', kmen)
print('количество ,больших максимального: ', kbol)


a = []
for c in range(10):
    print('Введите', c, 'элемент')
    a.append(int(input()))
sm = 0
for i in range(0, len(a)):
    if a[i]>5:
        sm += a[i]
print(sm)
